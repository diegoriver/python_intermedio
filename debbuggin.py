#### ejemplo con un numero
# def divisor():
#     divisor =[]
#     num = int(input("INgresa un numero: "))
#     for i in range(1,num+1):
#         if num % i == 0:
#             divisor.append(i)
#     return print(divisor)

# def run():
#     try:
#         divisor()
#         print("FIN")
#     except ValueError:
#         print("debes ingresar un numero")

# if __name__ == '__main__':
#     run()

### ejemplo Palindromo
def palindromo():
    string = input("ingrese una palabra: ")
    try:
        if len(string)==0:
            raise ValueError ("no se puede ingresar una cadena vacia")
        elif string == string[::-1]:
            mensaje = "Si es"
        else:
            mensaje = "NO es"
        return mensaje
    except ValueError as ve:
        print(ve)
        return string
        


def run():
    try:
        print (palindromo())
        print("FIN")
    except TypeError:
        print("debes ingresar un texto")


if __name__ == '__main__':
    run()
