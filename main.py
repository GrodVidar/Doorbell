import socket
import threading
import requests
from keys import *


def pushover_notification(title, message):
    url = 'https://api.pushover.net/1/messages.json'
    params = {
        'token': po_app_key,
        'user': po_user_key,
        'message': message,
        'device': 'OP8',
        'title': title
    }
    resp = requests.post(url, data=params)
    print(resp.text)


if __name__ == "__main__":
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    pushover_notification("Doorbell", "Initiated")
    server.bind(('', 12345))
    server.listen(5)
    while True:
        client, client_address = server.accept()
        print(f"{client_address} connected")
        c_online = True
        while c_online:
            c_message = client.recv(1024).decode('utf-8')
            print(c_message)
            pushover_notification("Doorbell", c_message)
            client.close()
            c_online = False
