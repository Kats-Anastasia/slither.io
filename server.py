import socket
from _thread import *
from snake import Snake
import pickle

server = "127.0.0.53"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for a connection, Server Started")


snakes = [Snake(), Snake()]

def threaded_client(conn, snake):
    conn.send(pickle.dumps(snakes[snake]))
    reply = ""
    while True:
        try:
            data = pickle.loads(conn.recv(2048))
            snakes[snake] = data

            if not data:
                print("Disconnected")
                break
            else:
                if snake == 1:
                    reply = snakes[0]
                else:
                    reply = snakes[1]

                print("Received: ", data)
                print("Sending : ", reply)

            conn.sendall(pickle.dumps(reply))
        except:
            break

    print("Lost connection")
    conn.close()

currentPlayer = 0
while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1
