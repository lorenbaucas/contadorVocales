import time
from multiprocessing import Process

def runA():
    nA = 0

    f = open("texto.txt")
    texto = f.read()

    for v in texto:
        if v in "aA":
            nA += 1
    f.close()
    print("A: "+str(nA))

def runE():
    nE = 0

    f = open("texto.txt")
    texto = f.read()

    for v in texto:
        if v in "eE":
            nE += 1
    f.close()
    print("E: "+str(nE))

def runI():
    nI = 0

    f = open("texto.txt")
    texto = f.read()

    for v in texto:
        if v in "iI":
            nI += 1
    f.close()
    print("I: "+str(nI))

def runO():
    nO = 0

    f = open("texto.txt")
    texto = f.read()

    for v in texto:
        if v in "oO":
            nO += 1
    f.close()
    print("O: "+str(nO))

def runU():
    nU = 0

    f = open("texto.txt")
    texto = f.read()

    for v in texto:
        if v in "uU":
            nU += 1
    f.close()
    print("U: "+str(nU))

if __name__ == '__main__':

    inicio = time.time()

    proceso = Process(target=runA())
    proceso.start()
    proceso.join()
    proceso = Process(target=runE())
    proceso.start()
    proceso.join()
    proceso = Process(target=runI())
    proceso.start()
    proceso.join()
    proceso = Process(target=runO())
    proceso.start()
    proceso.join()
    proceso = Process(target=runU())
    proceso.start()
    proceso.join()

    fin = time.time()
    print("El programa ha tardado: "+str(fin-inicio)+" segundos")