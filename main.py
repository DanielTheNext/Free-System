import time
import random
import math

menu_restaurant = []
menu_clients_new = []
op_chains = []
inventory = []
cart_menu = []
members_plus = ["SYSTEM", ""]
users_allowed = ["Kodland1", "Kodland2"]
products = []
discount_global_0 = []
discount_global_1 = []

def user_verification():
    global users_allowed

    print("******************************************************************************")
    print("*                                                                            *")
    print("*                     Sistema de Administracion                              *")
    print("*                                                                            *")
    print("******************************************************************************")
    print("******************************************************************************")
    print("*                                                                            *")
    print("*                          Ingrese el usuario:                               *")
    print("*                                                                            *")
    print("******************************************************************************")
    user_id = input("")
    

    if user_id not in users_allowed:
        print("Error 001: El usuario no es valido")
        raise TypeError
    

def ui_loader():
    print("******************************************************************************")
    print("*                                                                            *")
    print("*                         Sistema de Administracion                          *")
    print("*                                                                            *")
    print("******************************************************************************")
    print("******************************************************************************")
    print("*                                                                            *")
    print("*                                                                            *")
    print("*   1. Base de datos               2. Ventas                3. Inventario    *")
    print("*                                                                            *")
    print("*                                                                            *")
    print("*   4. Certificados                5. Server                6. Clientes      *")
    print("*                                                                            *")
    print("*                                                                            *")
    print("*                                                                            *")
    print("*                   7. Salir del panel administrativo                        *")
    print("******************************************************************************")
    option_api_0 = int(input("Elige Una opcion. "))
    if option_api_0 == 1:
        def data_loader():
            global members_plus
            print("******************************************************************************")
            print("*                                                                            *")
            print("*                         Sistema de Administracion                          *")
            print("*                                                                            *")
            print("******************************************************************************")
            print("******************************************************************************")
            print("*                                                                            *")
            print("*   1. Añadir miembros al club de pago Plus                                  *")
            print("*                                                                            *")
            print("*   2. Quitar miembros del club de pago Plus                                 *")
            print("*                                                                            *")
            print("*   3. Ver clientes del club de pago Plus                                    *")
            print("*                                                                            *")
            print("*   4. Salir del menu de base de datos                                       *")
            print("*                                                                            *")
            print("******************************************************************************")
            option_api_1 = int(input("Elige una opcion: "))
            if option_api_1 == 1:
                temporal_member_add = input("Introduce el nombre del cliente: ")
                members_plus.append(temporal_member_add)
                if "SYSTEM" in members_plus:
                    members_plus.remove("SYSTEM")
                    members_plus.append("SERVER_LINUX.FROM.PYTHON")
                    print("¡Cliente", temporal_member_add, "ha sido agregado correctamente al sistema de pago Plus!" )
                    data_continue_0 = input("Presione enter para continuar...")
                    data_loader()
                elif "SYSTEM" not in members_plus:
                    members_plus.append("SERVER_LINUX.FROM.PYTHON")
                    print("¡Cliente", temporal_member_add, "ha sido agregado correctamente al sistema de pago Plus!" )
                    data_continue_0 = input("Presione enter para continuar...")
                    data_loader()
            elif option_api_1 == 2:
                temporal_member_quit = input("Introduce el nombre del cliente a eliminar del club: ")
                if temporal_member_quit not in members_plus or temporal_member_quit == "None":
                    print("Error 003: el cliente no es valido")
                    data_continue_1 = input("Presione enter para continuar...")
                    data_loader()
                elif temporal_member_quit in members_plus and temporal_member_quit !=  "None":
                    members_plus.remove(temporal_member_quit)
                    members_plus.remove("SERVER_LINUX.FROM.PYTHON")
                    print("El cliente", temporal_member_quit, "ha sido eliminado satisfactoriamente del sistema.")
                    data_continue_2 = input("Presione enter para continuar...")
                    data_loader()
                elif temporal_member_quit == "None":
                    print("ERROR_CRITICAL: memory.system_not_quit")
                    data_continue_3 = input("Presione enter para continuar...")
                    data_loader()
            elif option_api_1 == 3:
                if "None" in members_plus:
                    print("Error 004: No hay ningun cliente asociado al club de pago Plus")
                    data_continue_4 = input("Presione enter para continuar...")
                    data_loader()
                else:
                    print("Los clientes afiliados son: ", members_plus, )
                    data_continue_5 = input("Presione enter para continuar...")
                    data_loader()
            elif option_api_1 == 4:
                ui_loader()


            if option_api_1 >= 4:
                print("Error 002: Esta opcion no existe:", option_api_0, )
                print(" ")
                print(" ")
                time.sleep(2)
                data_loader()
        data_loader()

    elif option_api_0 == 2:
        def ventas():
            global discount_global_0
            global discount_global_1
            global products
            print("******************************************************************************")
            print("*                                                                            *")
            print("*                         Sistema de Administracion                          *")
            print("*                                                                            *")
            print("******************************************************************************")
            print("******************************************************************************")
            print("*                                                                            *")
            print("*        1. Añadir una nueva venta           2. Version del sistema          *")
            print("*                                                                            *")
            print("*        3. Cupones aplicables               4. Salir de este menu           *")
            print("*                                                                            *")
            print("******************************************************************************")
            option_api_2 = int(input("Seleciona una opcion..."))
            if option_api_2 == 1:
                cliente = input("Ingrese el nombre del cliente: ")
                doc = input("Ingrese el numero de documento: ")
                pago = input("Ingrese el metodo de pago: ")
                ns = input("Ingrese el codigo de barras del producto")
                if ns in products:
                    print("Cargando compra y datos...")
                    time.sleep(3.2)
                    print("Pago completado")
                    data_continue_6 = input("Presiona enter para continuar...")
                    ventas()
                elif ns not in products:
                    print("Error 005: El producto no es valido")
                    data_continue_temp_new = input("Presione enter para continuar...")
                    ventas()
            elif option_api_2 == 2:
                print(" SYSTEM_INFORMATION")
                print("OS: Linux from Python")
                print("OS version: 14.5.903")
                print("BIOS VERSION: 60.71.0035")
                print("CORE_VERSION: 3.13")
                data_continue_7 = input("press enter to continue...")
                ventas()
            elif option_api_2 == 3:
                product = input("Ingrese el codigo de barras del producto: ")
                if product not in products:
                    print("Error 005: Este producto no existe")
                    data_continue_9 = input("Presione enter para continuar...")
                    ventas()
                elif product in discount_global_0:
                    print("Este producto tiene")
                    data_continue_10 = input("Presione enter para continuar...")
                    ventas()
                elif product in discount_global_1:
                    print("Este producto tiene")
                    data_continue_11 = input("Presione enter para continuar...")
                    ventas()
                elif product not in discount_global_0 and product not in discount_global_1:
                    print("Lo siento, este producto no tiene descuento")
                    data_continue_12 = input("Presione enter para continuar...")
                    ventas()
            elif option_api_2 == 4:
                ui_loader()
        ventas()
    elif option_api_0 == 3:
        def inventario():
            global inventory
            global cart_menu
            global menu_restaurant
            global menu_clients_new
            print("******************************************************************************")
            print("*                                                                            *")
            print("*                         Sistema de Administracion                          *")
            print("*                                                                            *")
            print("******************************************************************************")
            print("******************************************************************************")
            print("*                                                                            *")
            print("*   1. Ver el menu del restaurante     2. Añadir cosas al menu               *")
            print("*                                                                            *")
            print("*   3. Quitar cosas del menu           4. Verificar inventario               *")
            print("*                                                                            *")
            print("*   5. Cargar cosas al inventario      6. Quitar cosas al inventario         *")
            print("*                                                                            *")
            print("*                         7. Salir de este menu                              *")
            print("*                                                                            *")
            print("******************************************************************************")
            option_api_3 = int(input("Seleccione una opcion: "))
            if option_api_3 == 1:
                print("El menu de hoy en el restaurante es: ", menu_restaurant, )
                print("Los clientes han hecho el pedido de: ", menu_clients_new, )
                data_continue_12 = input("Presione enter para continuar...")
                inventario()
            elif option_api_3 == 2:
                temporal_menu_add = input("¿Que quieres añadir al menu? ")
                menu_restaurant.append(temporal_menu_add)
                data_continue_13 = input("Presione enter para continuar...")
                inventario()
            elif option_api_3 == 3:
                temporal_menu_quit = input("¿Que quieres quitar al menu? ")
                if temporal_menu_quit in menu_restaurant:
                    menu_restaurant.remove(temporal_menu_quit)
                    time.sleep(0.5)
                    print("", temporal_menu_quit, "ha sido quitado del menu satisfactoriamente.")
                    data_continue_14 = input("Presione enter para continuar...")
                    inventario()
                elif temporal_menu_quit not in menu_restaurant:
                    print("Error Temporal: Este objeto no se puede eliminar del menu porque no esta")
                    data_continue_14 = input("Presione enter para continuar...")
                    inventario()
            elif option_api_3 == 4:
                print("El inventario tiene: ", inventory, )
                data_continue_15 = input("Presione enter para continuar...")
                inventario()
            elif option_api_3 == 5:
                temporal_inventory_add = input("¿Que quieres agregar al inventario? ")
                inventory.append(temporal_inventory_add)
                time.sleep(0.5)
                print("", temporal_inventory_add, "ha sido quitado del menu satisfactoriamente.")
                data_continue_16 = input("Presione enter para continuar...")
                inventario()
            elif option_api_3 == 6:
                temporal_inventory_quit = input("¿Que quieres quitar del inventario? ")
                if temporal_inventory_quit not in inventory:
                    print("Error 006: El objeto no fue encontrado en el inventario")
                    data_continue_17 = input("Presione enter para continuar...")
                    inventario()
                elif temporal_inventory_quit in inventory:
                    inventory.remove(temporal_inventory_quit)
                    time.sleep(0.5)
                    print("El objeto fue quitado del inventario satisfactoriamente")
                    data_continue_18 = input("Presione enter para continuar...")
                    inventario()
            elif option_api_3 == 7:
                ui_loader()
        inventario()
    elif option_api_0 == 4:
        def certificate():
            print("******************************************************************************")
            print("*                                                                            *")
            print("*                         Sistema de Administracion                          *")
            print("*                                                                            *")
            print("******************************************************************************")
            print("******************************************************************************")
            print("*                                                                            *")
            print("*     Este sistema fue hehco por DanTechPro, un aficionado de Python.        *")
            print("*     Yo ciertamente pensaba que no serviria pero ahora me doy cuenta        *")
            print("*     que este sistema siempre valio la pena asi que por eso es que          *")
            print("*     tenemos certificados como: Python Awards 2026                          *")
            print("*                                                                            *")
            print("*                        1. Salir de este menu                               *")
            print("*                                                                            *")
            print("******************************************************************************")
            option_api_4 = int(input("Selecciona una opcion: "))
            if option_api_4 == 1:
                ui_loader()
        certificate()
    elif option_api_0 == 5:
        def auto_server():
            global members_plus
            server_conection = "SERVER_LINUX.FROM.PYTHON"
            if server_conection  not in members_plus:
                print("******************************************************************************")
                print("*                                                                            *")
                print("*                         Sistema de Administracion                          *")
                print("*                                                                            *")
                print("******************************************************************************")
                print("******************************************************************************")
                print("*                                                                            *")
                print("*                     El servidor esta desconectado                          *")
                print("*                                                                            *")
                print("*                         1. Salir de este menu                              *")
                print("*                                                                            *")
                print("******************************************************************************")
                option_api_temp_0 = int(input("Seleccione una opcion: "))
                if option_api_temp_0 == 1:
                    ui_loader()
            if server_conection in members_plus:
                print("******************************************************************************")
                print("*                                                                            *")
                print("*                         Sistema de Administracion                          *")
                print("*                                                                            *")
                print("******************************************************************************")
                print("******************************************************************************")
                print("*                                                                            *")
                print("*                       El servidor esta conectado                           *")
                print("*                                                                            *")
                print("*                         1. Salir de este menu                              *")
                print("*                                                                            *")
                print("******************************************************************************")
                option_api_temp_1 = int(input("Seleccione una opcion: "))
                if option_api_temp_1 == 1:
                    ui_loader()
        auto_server()
    elif option_api_0 == 6:
        def clients_menu():
            global op_chains
            global menu_clients_new
            global menu_restaurant
            print("******************************************************************************")
            print("*                                                                            *")
            print("*                         Sistema de clientes                                *")
            print("*                                                                            *")
            print("******************************************************************************")
            print("******************************************************************************")
            print("*                                                                            *")
            print("*          1. Poner una reseña           2. Ver las reseñas                  *")
            print("*                                                                            *")
            print("*          3. Ver el menu                4. Pedir algo del menu              *")
            print("*                                                                            *")
            print("*                       5. Salir de este menu                                *")
            print("*                                                                            *")
            print("******************************************************************************")
            option_api_client_1 = int(input("Selecciona una opcion: "))
            if option_api_client_1 == 1:
                op_chain = input("Escribe tu reseña: ")
                op_chains.append(op_chain)
                print("Reseña añadida satisfactoriamente")
                data_continue_temp_0 = input("Presione enter para continuar")
                clients_menu()
            elif option_api_client_1 == 2:
                print("Las reseñas son: ", op_chains, )
                data_continue_temp_1 = input("Presione enter para continuar")
                clients_menu()
            elif option_api_client_1 == 3:
                print("El menu de hoy es: ", menu_restaurant, )
                data_continue_temp_2 = input("Presione enter para continuar...")
                clients_menu()
            elif option_api_client_1 == 4:
                print("El menu de hoy es: ", menu_restaurant)
                menu_clients_temp = input("Que vas a pedir en el menu")
                time.sleep(0.5)
                if menu_clients_temp in menu_restaurant:
                    menu_clients_new.append(menu_clients_temp)
                    print("¡Tu pedido fue agregado satisfactoriamente al sistema!")
                    data_continue_temp_3 = input("Presione enter para continuar...")
                    clients_menu()
                else:
                    print("Error Text 001: La comida que quieres pedir no esta en el menu")
                    data_continue_temp_4 = input("Presione enter para continuar...")
                    clients_menu()
            elif option_api_client_1 == 5:
                user_verification()
                token_verification()
        clients_menu()

    if option_api_0 > 7:
        print("Error 002: Esta opcion no existe:", option_api_0, )
        data_continue_8 = input("Presiona enter para continuar...")
        ui_loader()

def token_verification():
    print("******************************************************************************")
    print("*                                                                            *")
    print("*                          Ingrese la contraseña:                            *")
    print("*                                                                            *")
    print("******************************************************************************")
    
    token_id = input("")
    
    if token_id == "5090332$@":
        ui_loader()
        
    else:
        token_verification()

user_verification()
token_verification()
