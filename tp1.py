import sys
from collections import deque

class Contrato:
    def __init__(self, numContrato, pos, radio):
        self.numContrato = numContrato
        self.pos = pos
        self.radio = radio

    def max(self):
        return (self.pos + self.radio)
    
    def min(self):
        return (self.pos - self.radio)
    
    def getNumeroContrato(self):
        return self.numContrato


def seSuperpone(contrato, k):
    return (contrato.min() <= k and contrato.max() >= k)


def encontrarMejoresContratos(listaContratos, km):

    listaContratos.sort(key=lambda e: e.min())
    contratos = deque(listaContratos)

    k = 0
    contratosSolucion = []
    tmp = 0

    while k < km and contratos:

        if seSuperpone(contratos[0], k):
            if tmp == 0 or  contratos[0].max() > tmp.max():
                tmp = contratos[0]
            contratos.popleft()
            
        else:
            if contratos[0].max() < k:
                contratos.popleft()
                continue
            else:
                if tmp == 0:
                    print("Error")
                    return None
                k = tmp.max()
                contratosSolucion.append(tmp)
                tmp = 0

    if tmp != 0:
        k = tmp.max()
        contratosSolucion.append(tmp)


    if k < km:
        print("Error")
        return None
    return contratosSolucion



def main():

    if(len(sys.argv) != 3):
        print("Error en los argumentos, debe ejecutarse el programa como: python tp1.py arg1 arg2")
        print("donde arg1 es el nombre del archivo con los contratos y arg2 es el largo de la ruta en km")
        print("Ej: python tp1.py contratos.txt 400")
        return 1

    listaContratos = []
    archivo = open(sys.argv[1])
    contenido = archivo.readlines()
    for line in contenido:
        linea = line.split(',')
        numContrato, pos, radio = [i.strip() for i in linea]
        contrato = Contrato(numContrato, int(pos), int(radio))
        listaContratos.append(contrato)
    archivo.close()

    solucion = encontrarMejoresContratos(listaContratos, int(sys.argv[2]))

    if solucion == None:
        print("No es posible hallar una solución con los contratos asignados para el largo de ruta dado.")
    else:
        print("contratos solucion:", end=" ")
        for i in solucion:
            print(i.getNumeroContrato(), end=" ")

main()