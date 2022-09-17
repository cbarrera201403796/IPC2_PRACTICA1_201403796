from api.structures.doublelinkedlist.DoubleLinkedList import DoubleLinkedList
from api.models.Client import Client
from api.models.Order import Order
from api.structures.Queue import Queue

menu_options = {
    1: 'Crear orden',
    2: 'Sacar orden',
    3: 'Generar reporte',
    4: 'Salir',
}

client_queue = Queue()


def print_menu():
    for key in menu_options.keys():
        print(key, '--', menu_options[key])


def option1():
    creating_order = True
    client_name = None
    client_phone = None
    quantity = None
    salchicha = None
    chorizo = None
    salami = None
    longaniza = None
    costilla = None

    orders = DoubleLinkedList()
    client = Client()

    while creating_order:
        if client_name is None:
            client_name = str(input('Ingrese nombre de cliente: '))
        elif client_phone is None:
            client_phone = str(input('Ingrese teléfono de cliente: '))
        elif quantity is None:
            quantity = int(input('Ingrese cantidad de shucos: '))
        else:
            print('Seleccion de ingredientes: ')
            if salchicha is None:
                salchicha = int(input('¿Quiere agregar salchicha? 1 = si | 2 = no: '))
                if salchicha != 1 and salchicha != 2:
                    salchicha = None
                    print('Solo puede elegir valores 1 o 2')
            elif chorizo is None:
                chorizo = int(input('¿Quiere agregar chorizo? 1 = si | 2 = no: '))
                if chorizo != 1 and chorizo != 2:
                    chorizo = None
                    print('Solo puede elegir valores 1 o 2')
            elif salami is None:
                salami = int(input('¿Quiere agregar salami? 1 = si | 2 = no: '))
                if salami != 1 and salami != 2:
                    salami = None
                    print('Solo puede elegir valores 1 o 2')
            elif costilla is None:
                costilla = int(input('¿Quiere agregar costilla? 1 = si | 2 = no: '))
                if costilla != 1 and costilla != 2:
                    costilla = None
                    print('Solo puede elegir valores 1 o 2')
            elif longaniza is None:
                longaniza = int(input('¿Quiere agregar costilla? 1 = si | 2 = no: '))
                if longaniza != 1 and costilla != 2:
                    longaniza = None
                    print('Solo puede elegir valores 1 o 2')
            else:
                if salchicha == 2 and salami == 2 and chorizo == 2 and costilla == 2 and longaniza == 2:
                    print('Debe elegir al menos un ingrediente')
                    salchicha = None
                    chorizo = None
                    salami = None
                    longaniza = None
                    costilla = None

                else:
                    orders.add(
                        Order(has_salami=salami, has_chorizo=chorizo, has_costilla=costilla, has_longaniza=longaniza,
                              has_salchicha=salchicha, quantity=quantity))
                    add_more = int(input('¿Desea agregár más shukos a la orden?  1 = si | 2 = no:'))
                    if add_more == 1:
                        salchicha = None
                        chorizo = None
                        salami = None
                        longaniza = None
                        costilla = None
                        quantity = None
                    elif add_more == 2:
                        client.name = client_name
                        client.orders = orders
                        client.phone = client_phone
                        client_queue.enqueue(client)
                        creating_order = False


def option2():
    print('Handle option \'Option 2\'')


def option3():
    print('Handle option \'Option 3\'')


if __name__ == '__main__':
    while True:
        print_menu()
        option = ''
        try:
            option = int(input('Ingrese su opción: '))
        except:
            print('Entrada incorrecta, ingrese un número ...')
        # Check what choice was entered and act accordingly
        if option == 1:
            option1()
        elif option == 2:
            option2()
        elif option == 3:
            option3()
        elif option == 4:
            print('Se ha terminado la aplicación')
            exit()
        else:
            print('Opción inválida seleccione una entre  1 y 4.')
