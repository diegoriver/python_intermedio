class Persona:
    def __init__ (self, nombre):
        self.nombre = nombre

    def avanza (self):
        print(f'{self.nombre} esta caminando')

class Ciclista (Persona):
    def __init__(self, nombre):
        super().__init__(nombre)

    def avanza(self):
        print(f'{self.nombre} anda en bicicleta')


if __name__=='__main__':
    people1 = Persona('Caliche')
    people2 = Ciclista('mi perrito')
    print(people1.nombre)
    people1.avanza()
    print(people2.nombre)
    people2.avanza()
