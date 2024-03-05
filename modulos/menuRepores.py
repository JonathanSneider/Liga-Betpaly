import os
def menuReportes():
    lstopciones = ['A','B','C','D','E','F']
    opciones = ['A. Equipo Goleador','B, Equipo con mayor puntaje','C. Equipo que mas partidos gano','D. Total de goles anotados por todos los equipo','E. Promedio de goles anotados en el torneo','F. Salir a menu principal']
    titulo = """
        ++++++++++++++++++++++++++++++++++
        +      LIGA BETPLAY REPORTES     +
        ++++++++++++++++++++++++++++++++++
    """
    print(titulo)
    for item in opciones:
        print(item)
    try:
        op = input('Seleccione una opcion: ').upper()
    except:
        print('Error intentelo otra vez')
        os.system('pause')
        menuReportes()
    else:
        return op
        
    
    
