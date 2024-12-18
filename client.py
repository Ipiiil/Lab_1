import socket
import time

def start_client():
    while True:
        try:
            # Создаем сокет
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            # Подключение к серверу
            client_socket.connect(('localhost', 12345))

            # Создание запроса
            request = "ping"
            print(f"Отправка запроса: {request}")

            # Отправка запроса
            client_socket.sendall(request.encode('utf-8'))

            # Ожидание ответа
            response_data = client_socket.recv(1024)
            response = response_data.decode('utf-8')

            # Чтение и обработка ответа
            if response.strip() == "pong":
                print(f"Получен ответ: {response}")
            else:
                print("Ошибка: неожиданный ответ от сервера")

        except Exception as e:
            # Обработка ошибок
            print(f"Ошибка: {e}")

        finally:
            # Закрытие сокета
            client_socket.close()

        # Повторить цикл
        time.sleep(1)

if __name__ == "__main__":
    start_client()

