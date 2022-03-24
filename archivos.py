

from tkinter.font import names


def leer():
    numeros =[]
    with open("./archivos/numbers.txt","r", encoding="utf-8") as f:
        for line in f:
            numeros.append(int(line))
    print (numeros)

def escribir():
    nombres =["mis perritos","canchosos","morronga"]
    with open("./archivos/names.txt", "a", encoding="utf-8") as a:
        for name in nombres:
            a.write(name)
            a.write("\n")



def run():
    leer()
    escribir()

if __name__ == '__main__':
    run()