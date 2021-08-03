import socket
import threading
from pushbullet import Pushbullet
from dotenv import load_dotenv
import os

def accept_connections():
    while True:
        client, client_address = server.accept()
        print(f"{client_address} connected")
        c_online = True
        while c_online:
            message = client.recv(1024).decode('utf-8')
            print(message)
            dev.push_note('Doorbell', message)
            client.close()
            c_online = False


if __name__ == "__main__":
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    pb_key = os.getenv('PUSHBULLET_KEY')
    pb = Pushbullet(pb_key)
    dev = pb.get_device('OnePlus IN2023')
    dev.push_note('Doorbell', 'activated')
    server.bind(('', 12345))
    server.listen(5)
    acc_thread = threading.Thread(target=accept_connections)
    acc_thread.start()
