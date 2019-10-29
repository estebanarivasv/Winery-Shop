class PurchaseOrder():

    def __init__(self, code = 0, payment = '', date = '', product = [], cost = [], quantity = [], total = 0.0):
        self.__code = code
        self.__payment = payment
        self.__date = date
        self.__product = product
        self.__cost = cost
        self.__quantity = quantity
        self.__total = total

    def setCode(self, new_code):
        self.__code = new_code

    def setPayment(self, new_payment):
        self.__payment = new_payment

    def setDate(self, new_date):
        self.__date = new_date

    def setProduct(self, new_product):
        self.__product = new_product

    def setCost(self, new_cost):
        self.__cost = new_cost

    def setQuantity(self, new_quantity):
        self.__quantity = new_quantity

    def setTotal(self):
        return self.__total

    def getCode(self):
        return self.__code

    def getPayment(self):
        return self.__payment

    def getDate(self):
        return self.__date

    def getProduct(self, num):
        return self.__product[num]

    def getCost(self, num):
        return self.__cost[num]

    def getQuantity(self, num):
        return self.__quantity[num]

    def getTotal(self):
        return self.__total

def saveLenght(n):
    global count
    count = n

def addPurchaseOrder():
    print('\nIngrese los datos de la orden de compra: ')
    code = int(input('Código: '))
    payment = input('Forma de pago: ')
    date = input('Fecha: ')
    p = []
    c = []
    q = []
    tot = 0
    t = 0
    while True:
        pro = input('Nombre del producto: ')
        p.append(pro)
        cos = float(input('Costo: '))
        c.append(cos)
        qua = int(input('Cantidad: '))
        q.append(qua)
        res = qua * cos
        tot = res + tot
        t = t + 1
        saveLenght(t)
        op = int(input('¿Desea seguir agregando productos? (1- Si, 2- No): '))
        if op == 1:
            pass
        elif op == 2:
            break
    purchase.append(PurchaseOrder(code, payment, date, p, c, q, tot))

def deletePurchaseOrder():
    listPurchaseOrder()
    op = int(input('\nSeleccione el numero de la orden de compra que desea borrar: '))
    purchase.pop(op - 1)

def editPurchaseOrder():
    listPurchaseOrder()
    op = int(input('\nSeleccione el numero de la orden de compra que desea editar: '))
    p = op - 1
    print('\n¿Qué desea editar?'
          '\n1.	Código',
          '\n2.	Forma de pago',
          '\n3.	Fecha',
          '\n4.	Productos')
    sel = int(input('Opción: '))
    if sel == 1:
        code = int(input('Nuevo código: '))
        purchase[p].setCode(code)
    elif sel == 2:
        payment = input('Nueva forma de pago: ')
        purchase[p].setPayment(payment)
    elif sel == 3:
        date = input('Nueva fecha: ')
        purchase[p].setDate(date)
    elif sel == 4:
        while True:
            pro = input('Nombre del producto: ')
            p.append(pro)
            cos = float(input('Costo: '))
            c.append(cos)
            qua = int(input('Cantidad: '))
            q.append(qua)
            res = qua * cos
            tot = res + tot
            t = t + 1
            saveLenght(t)
            op = int(input('¿Desea seguir agregando productos? (1- Si, 2- No): '))
            if op == 1:
                pass
            elif op == 2:
                break
        purchase[p].setProduct(pro)
        purchase[p].setCost(cos)
        purchase[p].setQuantity(qua)
        purchase[p].setTotal(t)

        print(
            f'\nNro. Orden: {p + 1}'
            f'\nCódigo: {purchase[p].getCode()}',
            '\nProductos: '
        )
        for p in range(count):
            print('\tNro: ', p + 1,
                  '\tNombre: ', purchase[p].getProduct(p),
                  '\tCosto unitario: ', purchase[p].getCost(p),
                  '\tCantidad: ', purchase[p].getQuantity(p))
        print(
            '\nMedio de pago: ', purchase[p].getPayment(),
            '\nFecha: ', purchase[p].getDate(),
            '\nCosto total: ', purchase[p].getTotal(),
            '\n\n'
        )


def listPurchaseOrder():
    for p in range(len(purchase)):
        print(
            f'\nNro. Orden: {p + 1}'
            f'\nCódigo: {purchase[p].getCode()}',
            '\nProductos: '
        )
        for i in range(count):
            print('\tNro: ', i + 1,
                  '\tNombre: ', purchase[p].getProduct(i),
                  '\tCosto unitario: ', purchase[p].getCost(i),
                  '\tCantidad: ', purchase[p].getQuantity(i))
        print(
            '\nMedio de pago: ', purchase[p].getPayment(),
            '\nFecha: ', purchase[p].getDate(),
            '\nCosto total: ', purchase[p].getTotal(),
            '\n\n'
        )


purchase = []
