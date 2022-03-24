import random


def busqueda_binaria(lista, comienzo, final, objetivo,a=0):
    print(f'buscando {objetivo} entre {lista[comienzo]} y {lista[final - 1]}')
    a+=1
    if comienzo > final:
        return False, a
    
    medio = (comienzo + final) // 2

    if lista [medio] == objetivo:
        return True, a
    elif lista [medio] < objetivo:
        return busqueda_binaria(lista, medio+1, final, objetivo)
    else:
        return busqueda_binaria(lista, comienzo, medio-1,objetivo)
 


if __name__ == '__main__':
    tamano_lista = int(input('tamano lista '))
    objetivo = int(input('numero a encontrar '))

    lista = sorted([random.randint(0, 100) for i in range(tamano_lista)])

    encontrado = busqueda_binaria(lista, 0, len(lista), objetivo)
    print(lista)
    print(f'el elemento {objetivo} {"esta" if encontrado [0] else "no esta"} en la lista')
    print(f'No iteraciones: {encontrado[1]}')
