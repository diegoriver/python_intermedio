### ejemplo con un numero
def divisor():
    divisor =[]
    num = input("INgresa un numero: ")
    assert num.isnumeric(),"debes ingresar un numero"
    num=int(num)
    for i in range(1,num+1):
        if num % i == 0:
            divisor.append(i)
    return print(divisor)

def run():
        divisor()
        print("FIN")


if __name__ == '__main__':
    run()
