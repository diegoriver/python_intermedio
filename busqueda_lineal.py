import random

def busqueda_lineal(lista, objetivo):
    match = False
    a=1

    for elemento in lista:
        if elemento == objetivo:
            match = True
            break
        a+=1
    
    return match,a

if __name__=='__main__':
    tamano_lista = int(input('tamano lista '))
    objetivo = int(input('numero a encontrar '))

    lista = [random.randint (0,100) for i in range(tamano_lista)]

    encontrado = busqueda_lineal(lista, objetivo)
    print(lista)
    print(f'el elemento {objetivo} {"esta" if encontrado[0] else "no esta"} en la lista')
    print(f'No iteraciones: {encontrado[1]}')

