import time

def contar_vocales():


    f = open ("texto.txt")
    texto = f.read()

    nA = 0
    nE = 0
    nI = 0
    nO = 0
    nU = 0

    for v in texto:
        if v in "aA":
            nA += 1
        if v in "eE":
            nE += 1
        if v in "iI":
            nI += 1
        if v in "oO":
            nO += 1
        if v in "uU":
            nU += 1

    f.close()

    print   ("Total: " + str(nA+nE+nI+nO+nU) + "\n" +
             "A: " + str(nA) + "\n" +
             "E: " + str(nE) + "\n" +
             "I: " + str(nI) + "\n" +
             "O: " + str(nO) + "\n" +
             "U: " + str(nU) + "\n")

if __name__ == '__main__':

    inicio = time.time()

    contar_vocales()

    fin = time.time()
    print("El programa ha tardado: "+str(fin-inicio)+" segundos")