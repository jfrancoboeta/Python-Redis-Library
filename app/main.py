import socket
import threading


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    while True:
        conn, addr = server_socket.accept()  # wait for client
        threading.Thread(target=handle_client, args=(conn, addr)).start()

def handle_data(data):
    decoded = data.decode().split("\r\n")
    decodedArr = decoded[1:][1::2]
    print(decodedArr)
    return decodedArr

def handle_client(conn, addr):
    while True:
        data = handle_data(conn.recv(1024))
        if data[0] == "ping":
            res = "+PONG\r\n"
            conn.send(res.encode())
        elif data[0] == "echo":
            res = data[1]
            response = f"${len(data[1])}\r\n{res}\r\n"
            conn.send(response.encode())
        elif not data:
            conn.close()
            break


if __name__ == "__main__":
    main()
