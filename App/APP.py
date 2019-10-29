import Clients
from Clients import addClient
from Clients import deleteClient
from Clients import editClient
from Clients import listClient
import Products
from Products import addProduct
from Products import deleteProduct
from Products import editProduct
from Products import listProduct
import PurchaseOrder
from PurchaseOrder import addPurchaseOrder
from PurchaseOrder import deletePurchaseOrder
from PurchaseOrder import editPurchaseOrder
from PurchaseOrder import listPurchaseOrder
import Wines
from Wines import addWine
from Wines import deleteWine
from Wines import editWine
from Wines import listWine

def products():
    while True:
        print(
            "\n\n\tPRODUCTOS "
            "\n 1. Añadir un nuevo producto"
            "\n 2. Borrar un producto añadido"
            "\n 3. Editar productos"
            "\n 4. Ver productos"
            "\n 5. Sección vinos"
            "\n 6. Atrás")
        op = int(input("Opcion: "))
        if op == 1:
            addProduct()
        elif op == 2:
            deleteProduct()
        elif op == 3:
            editProduct()
        elif op == 4:
            listProduct()
        elif op == 5:
            wines()
        elif op == 6:
            break
        else:
            print('Opcion incorrecta. Intente nuevamente.')


def wines():
    while True:
        print(
            "\n\n\tVINOS"
            "\n 1. Añadir un nuevo vino"
            "\n 2. Borrar un vino añadido"
            "\n 3. Editar vinos"
            "\n 4. Ver vinos"
            "\n 5. Atrás")
        op = int(input("Opcion: "))
        if op == 1:
            addWine()
        elif op == 2:
            deleteWine()
        elif op == 3:
            editWine()
        elif op == 4:
            listWine()
        elif op == 5:
            break
        else:
            print('Opcion incorrecta. Intente nuevamente.')


def clients():
    while True:
        print(
            "\n\n\tCLIENTES "
            "\n 1. Añadir un nuevo cliente"
            "\n 2. Borrar un cliente añadido"
            "\n 3. Editar clientes"
            "\n 4. Ver clientes"
            "\n 5. Atrás")
        op = int(input("Opcion: "))
        if op == 1:
            addClient()
        elif op == 2:
            deleteClient()
        elif op == 3:
            editClient()
        elif op == 4:
            listClient()
        elif op == 5:
            break
        else:
            print('Opcion incorrecta. Intente nuevamente.')


def purchaseorder():
    while True:
        print(
            "\n\n¿Qué desea hacer?: "
            "\n 1. Añadir una nueva órden de compra"
            "\n 2. Borrar una órden de compra añadida"
            "\n 3. Editar órdenes de compra"
            "\n 4. Ver órdenes de compra"
            "\n 5. Atrás")
        op = int(input("Opcion: "))
        if op == 1:
            addPurchaseOrder()
        elif op == 2:
            deletePurchaseOrder()
        elif op == 3:
            editPurchaseOrder()
        elif op == 4:
            listPurchaseOrder()
        elif op == 5:
            break
        else:
            print('Opcion incorrecta. Intente nuevamente.')


# CODIGO PRINCIPAL

while True:
    print("Vinoteca 'Sabores Mendocinos'"
          "\n¡Bienvenido!"
          "\n¿A dónde desea acceder?"
          "\n1. Productos"
          "\n2. Clientes"
          "\n3. Órdenes de compra"
          "\n4. Salir")
    num = int(input('Opción: '))
    if num == 1:
        products()
    elif num == 2:
        clients()
    elif num == 3:
        purchaseorder()
    elif num == 4:
        print('Gracias por utilizar este servicio')
        break
    else:
        print('\nOpción incorrecta. Intente nuevamente.')


