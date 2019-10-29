class Client:

    def __init__(self, name = "", surname = "", code = 0, dni = 0, address = "", email = ""):
        self.__name = name
        self.__surname = surname
        self.__code = code
        self.__dni = dni
        self.__address = address
        self.__email = email

    def setName(self, new_name):
        self.__name = new_name

    def setSurname(self, new_surname):
        self.__surname = new_surname

    def setCode(self, new_code):
        self.__code = new_code

    def setDni(self, new_dni):
        self.__dni = new_dni

    def setAddress(self, new_address):
        self.__address = new_address

    def setEmail(self, new_email):
        self.__email = new_email

    def getName(self):
        return self.__name

    def getSurname(self):
        return self.__surname

    def getCode(self):
        return self.__code

    def getDni(self):
        return self.__dni

    def getAddress(self):
        return self.__address

    def getEmail(self):
        return self.__email

def listClient():
    for i in range(len(client)):
        print('\n','Numero cliente: ', i + 1, '\n',
              'Nombre: ', client[i].getName(), '\n',
              'Apellido: ', client[i].getSurname(), '\n',
              'Código: ', client[i].getCode(), '\n',
              'D.N.I: ', client[i].getDni(), '\n',
              'Dirección: ', client[i].getAddress(), '\n',
              'E-Mail: ', client[i].getEmail())

def addClient():
    print('Ingrese los datos del cliente: \n')
    name = input('Nombre: ')
    surname = input('Apellido: ')
    code = int(input('Código: '))
    dni = int(input('DNI: '))
    address = input('Direccion: ')
    email = input('E-Mail: ')
    client.append(Client(name, surname, code, dni, address, email))
    return

def deleteClient():
    listClient()
    op = int(input('\nSeleccione el numero del cliente que desea borrar: '))
    client.pop(op-1)

def editClient():
    listClient()
    op = int(input('\nSeleccione el numero del cliente que desea editar: '))
    cl = op - 1
    selection = int(input('\n¿Qué desea editar?\n1. Nombre\n2. Apellido\n3. Codigo\n4. D.N.I\n5. Dirección\n6. E-Mail\n Opcion: '))
    if selection == 1:
        name = input('Nuevo Nombre: ')
        client[cl].setName(name)
    elif selection == 2:
        surname = input('Nuevo Apellido: ')
        client[cl].setSurname(surname)
    elif selection == 3:
        code = int(input('Nuevo Código: '))
        client[cl].setCode(code)
    elif selection == 4:
        dni = int(input('Nuevo DNI: '))
        client[cl].setDni(dni)
    elif selection == 5:
        address = input('Nueva Direccion: ')
        client[cl].setAddress(address)
    elif selection == 6:
        email = input('Nuevo E-Mail: ')
        client[cl].setEmail(email)
    else:
        print('Opcion incorrecta. Intente nuevamente.')
    print('\n', 'Numero cliente: ', cl + 1, '\n',
          'Nombre: ', client[cl].getName(), '\n',
          'Apellido: ', client[cl].getSurname(), '\n',
          'Código: ', client[cl].getCode(), '\n',
          'D.N.I: ', client[cl].getDni(), '\n',
          'Dirección: ', client[cl].getAddress(), '\n',
          'E-Mail: ', client[cl].getEmail())


client = []


