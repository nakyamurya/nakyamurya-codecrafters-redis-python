# Uncomment this to pass the first stage
import socket


def main():
    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    client_connection, _ = server_socket.accept()

    while True:
        try:
            message_receive = client_connection.recv(1024)
            message_send = b"+PONG\r\n"
            client_connection.send(message_send)
        except ConnectionResetError:
            break
        except BrokenPipeError:
            break
    client_connection.close()
        

if __name__ == "__main__":
    main()
