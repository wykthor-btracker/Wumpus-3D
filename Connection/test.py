
import numpy as np


def mapping(string_map,dimension):
    protocolo = string_map
    x = protocolo.split()
    x1 = x[4].replace("[","")
    x2 = x1.replace("]","")
    mapa = np.fromstring(x2,dtype = int, sep = ",")
    return mapa

def main():
    print(mapping("INIC nome: wykthor mapa: [[0,1,0,1],[0,1,0,1],[0,1,0,1],[0,0,0,1]]",4))

main()




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