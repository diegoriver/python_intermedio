import random

def escribirPalabra(d, indices, letra):
#    p = list(palabra) #convierte la palabra en list
    for x in range(len(indices)):
        d[indices[x]] = letra
    print(d)
#    print(indices)
    return d
    
def encontrarLetra(palabra,letra):
    indices = [index for index in range(
        len(palabra)) if palabra[index] == letra]
    #print(indices)
    return indices

def cargarArchivo():
    archivo=[]
    with open("./archivos/names.txt", "r", encoding="utf-8") as f:
        for line in f:
            archivo.append(line)
        return archivo

def run():
    archivo = cargarArchivo()
    a= random.randint(0, len(archivo)-1)
    palabra = archivo[a]
    print(palabra)
    d = list("_"*(len(palabra)-1))  # crea la palabra "_ " en list
    a=0
    while a<10:
        letra = input("escriba su letra: ")
        indices = encontrarLetra(palabra, letra)
        escribirPalabra(d, indices, letra)
        a=a+1

if __name__ == '__main__':
    run()


