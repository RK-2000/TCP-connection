import threading
import socket

nickname = input("Choose your nickname: ")

# Connecting To Server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 55555))


def receive():
    while True:
        try:     
            message = client.recv(1024).decode('ascii')
            if message == '1234':
                client.send(nickname.encode('ascii'))
            else:
                
                if message.split(":")[0] == nickname:
                    message = 'Me:' + message.split(":")[1]
                print(message)
        except:
            # Close Connection When Error
            print("An error occured!")
            client.close()
            break

def write():
    while True:
        message = '{}: {}'.format(nickname, input(''))
        client.send(message.encode('ascii'))

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()