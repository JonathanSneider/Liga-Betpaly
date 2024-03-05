import os

def crear_menu():
    ltsopcion = [1,2,3,4]
    titulo = """
    ++++++++++++++++++++++++++++++++++
    +      LIGA BETPLAY MENU         +
    ++++++++++++++++++++++++++++++++++
    
    """
    
    print(titulo)
    
    try:
        opciones = '1. Agregar equipo\n2. Regristrar Fecha\n3. Reportes\n4. Salir'
        print(opciones)
        op = int(input("Seleccione una opción: "))
        if (op not in ltsopcion):
            crear_menu()
        
    except ValueError:
        print('Dato invalido')
        os.system('pause')
        crear_menu()
        
    else:
        return op
    

