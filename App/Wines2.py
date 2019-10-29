from Products import Products

class Wines(Products):

    #En el init si vos haces cosas como age = 0, despues cuando instancias el objeto y 
    # le pasas un parametro no te lo va a tomar, se va a reemplazar por 0 o a lo que lo hayas igualado dentro del init
    # lo tenes que dejar como lo puse  para que pasarle los valores a los atributos
    def __init__(self,  cellar, age, variety, country):
        super(Wines, self).__init__()
        self.__cellar = cellar
        self.__age = age
        self.__variety = variety
        self.__country = country

    def setCellar(self, new_cellar):
        self.__cellar = new_cellar

    def setAge(self, new_age):
        self.__age = new_age

    def setVariety(self, new_variety):
        self.__variety = new_variety

    def setCountry(self, new_origin):
        self.__origin = new_origin

    def getCellar(self):
        return self.__cellar

    def getAge(self):
        return self.__age

    def getVariety(self):
        return self.__variety

    def getCountry(self):
        return self.__country

def listWine():
    for i in range(len(wine)):
        print(
            '\nEjemplar nro: ', i+1,
            '\nNombre: ', wine[i].getName(),
            '\nCódigo: ', wine[i].getCode(),
            '\nCosto: ', wine[i].getCost(),
            '\nMarca: ', wine[i].getBrand(),
            '\nStock: ', wine[i].getStock(),
            '\nTipo de envase: ', wine[i].getContainer(),
            '\nBodega: ', wine[i].getCellar(),
            '\nEdad del vino: ', wine[i].getAge(),
            '\nVarietal: ', wine[i].getVariety(),
            '\nPais de origen: ', wine[i].getCountry())

def addWine():
    print('Ingrese los datos del ejemplar: \n')
    name = input('Nombre: ')
    code = int(input('Codigo: '))
    cost = float(input('Costo: '))
    brand = input('Marca: ')
    stock = int(input('Cantidad de Stock: '))
    container_type = input('Tipo de envase: ')
    cellar = input('Bodega: ')
    age = int(input('Año: '))
    variety = input('Varietal: ')
    country = input('Pais de origen: ')
    #Aca en vez de tratar de hacer un append de una, primero instancio el vino con el nombre new_wine y le paso los 4 parametros del init
    new_wine = Wines(cellar, age, variety, country)
    # y despues de instanciarlo le voy cambiando los atributos que hereda de la clase padre con los sets
    new_wine.setName(name)
    new_wine.setCode(code)
    new_wine.setStock(stock)
    new_wine.setCost(cost)
    new_wine.setBrand(brand)
    new_wine.setContainer(container_type)
    #y esa ultima linea lo agrega a la lista de vinos
    wine.append(new_wine)
    return

def deleteWine():
    listWines()
    op = int(input('\nSeleccione el numero del ejemplar que desea borrar: '))
    wine.pop(op-1)

def editWine():
    listWine()
    op = int(input('\nSeleccione el numero del ejemplar que desea editar: '))
    w = op - 1
    selection = int(input('\n¿Qué desea editar?'
                          '\n1.	Nombre',
                          '\n2.	Codigo',
                          '\n3.	Costo',
                          '\n4.	Marca',
                          '\n5.	Cantidad de Stock',
                          '\n6.	Tipo de envase',
                          '\n7.	Bodega',
                          '\n8.	Año',
                          '\n9.	Varietal',
                          '\n10.	Pais de origen',
                          '\n\nOpcion: '))
    if selection == 1:
        name = input('Nuevo Nombre: ')
        wine[w].setName(name)
    elif selection == 2:
        code = int(input('Nuevo Codigo: '))
        wine[w].setCode(code)
    elif selection == 3:
        cost = float(input('Nuevo Costo: '))
        wine[w].setCost(cost)
    elif selection == 4:
        brand = input('Nueva Marca: ')
        wine[w].setBrand(brand)
    elif selection == 5:
        stock = int(input('Nuevo Cantidad de Stock: '))
        wine[w].setStock(stock)
    elif selection == 6:
        container_type = input('Nuevo Tipo de envase: ')
        wine[w].setContainer(container_type)
    elif selection == 7:
        cellar = input('Nueva Bodega: ')
        wine[w].setCellar(cellar)
    elif selection == 8:
        age = int(input('Nuevo Año: '))
        wine[w].setAge(age)
    elif selection == 9:
        variety = input('Nuevo Varietal: ')
        wine[w].setVariety(variety)
    elif selection == 10:
        country = input('Nuevo Pais de origen: ')
        wine[w].setCountry(country)
    else:
        print('Opcion incorrecta. Intente nuevamente.')
    print(
        '\nEjemplar nro: ', w + 1,
        '\nNombre: ', wine[w].getName(),
        '\nCódigo: ', wine[w].getCode(),
        '\nCosto: ', wine[w].getCost(),
        '\nMarca: ', wine[w].getBrand(),
        '\nStock: ', wine[w].getStock(),
        '\nTipo de envase: ', wine[w].getContainer(),
        '\nBodega: ', wine[w].getCellar(),
        '\nEdad del vino: ', wine[w].getAge(),
        '\nVarietal: ', wine[w].getVariety(),
        '\nPais de origen: ', wine[w].getCountry())
wine = []
