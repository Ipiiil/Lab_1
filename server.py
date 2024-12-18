import socket

def start_server():
    # Создаем сокет
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Привязываем сокет к IP адрес и порту
    server_socket.bind(('localhost', 12345))

    # Начинаем прослушивать запросы
    server_socket.listen(1)

    print("Сервер запущен и ожидает подключений...")

    while True:
        # Принятие подключения
        client_socket, addr = server_socket.accept()

        try:
            print(f"Подключен клиент: {addr}")

            # Ожидание запроса
            data = client_socket.recv(1024)
            if data:
                request = data.decode('utf-8')
                print(f"Получен запрос: {request}")

                if request.strip() == "ping":
                    # Обработка запроса и отправка ответа
                    response = "pong"
                    client_socket.sendall(response.encode('utf-8'))
                else:
                    # Обнаружена ошибка (неожиданное сообщение)
                    print("Ошибка: Неверный запрос")

        finally:
            # Закрываем соединение с клиентом
            client_socket.close()

if __name__ == "__main__":
    start_server()

