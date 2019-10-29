class Products:

    def __init__(self, name = '', code = 0, cost = 0.0, brand = '', stock = 0, container_type = ''):
        self.__name = name
        self.__code = code
        self.__cost = cost
        self.__brand = brand
        self.__stock = stock
        self.__container_type = container_type

    def setName(self, new_name):
        self.__name = new_name

    def setCode(self, new_code):
        self.__code = new_code

    def setCost(self, new_cost):
        self.__cost = new_cost

    def setBrand(self, new_brand):
        self.__brand = new_brand

    def setStock(self, new_stock):
        self.__stock = new_stock

    def setContainer(self, new_container):
        self.__container_type = new_container

    def getName(self):
        return self.__name

    def getCode(self):
        return self.__code

    def getCost(self):
        return self.__cost

    def getBrand(self):
        return self.__brand

    def getStock(self):
        return self.__stock

    def getContainer(self):
        return self.__container_type

def addProduct():
    print('Ingrese los datos del producto: \n')
    name = input('Nombre: ')
    code = int(input('Codigo: '))
    cost = float(input('Costo: '))
    brand = input('Marca: ')
    stock = int(input('Cantidad de Stock: '))
    container_type = input('Tipo de envase: ')
    products.append(Products(name, code, cost, brand, stock, container_type))

def deleteProduct():
    listProduct()
    op = int(input('\nSeleccione el numero del producto que desea borrar: '))
    products.pop(op - 1)

def editProduct():
    listProduct()
    op = int(input('\nSeleccione el numero del producto que desea editar: '))
    p = op - 1
    print('\n¿Qué desea editar?'
          '\n1.	Nombre',
          '\n2.	Codigo',
          '\n3.	Costo',
          '\n4.	Marca',
          '\n5.	Cantidad de Stock',
          '\n6.	Tipo de envase')
    selection = int(input('Opcion: '))
    if selection == 1:
        name = input('Nuevo Nombre: ')
        products[p].setName(name)
    elif selection == 2:
        code = int(input('Nuevo Codigo: '))
        products[p].setCode(code)
    elif selection == 3:
        cost = float(input('Nuevo Costo: '))
        products[p].setCost(cost)
    elif selection == 4:
        brand = input('Nueva Marca: ')
        products[p].setBrand(brand)
    elif selection == 5:
        stock = int(input('Nuevo Cantidad de Stock: '))
        products[p].setStock(stock)
    elif selection == 6:
        container_type = input('Nuevo Tipo de envase: ')
        products[p].setContainer(container_type)

def listProduct():
    for i in range(len(products)):
        print(
            '\nEjemplar nro: ', i + 1,
            '\nNombre: ', products[i].getName(),
            '\nCódigo: ', products[i].getCode(),
            '\nCosto: ', products[i].getCost(),
            '\nMarca: ', products[i].getBrand(),
            '\nStock: ', products[i].getStock(),
            '\nTipo de envase: ', products[i].getContainer())

products = []