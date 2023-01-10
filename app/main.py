# Uncomment this to pass the first stage
import socket


def main():
    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    client_connection, _ = server_socket.accept()
    client_connection.recv(1024)
    client_connection.send(b"+PONG\r\n")


if __name__ == "__main__":
    main()
