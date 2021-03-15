#!/usr/bin/env python3

import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)
#%%
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(4096)
            if not data:
                break
            print(len(data))
            conn.sendall(data)

"""INIC
nome: wykthor
mapa: [[0,1,j,1],[0,1,0,1],[0,1,0,1],[0,m,0,1]] -> numpy.array

"""
"""
PROX
ID: x235
jogada: (2,1)

PROX (Servidor -> cliente)
jogada: (2,3)

FIM
vencedor: monstro
pontuaçãoJ: x
pontuaçãoM: y


"""