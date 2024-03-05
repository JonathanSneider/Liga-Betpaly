import os
import modulos.menu as mp
import modulos.menuRepores as mr 
import modulos.equipos as e 

if __name__ == "__main__":
    equipossliga = []
    mp.crear_menu
    isAppRunning = True
    while isAppRunning:
        op = mp.crear_menu()
        if op == 1:
            isAddTeam = True
            while isAddTeam:
                e.os.system('cls')
                e.AddTeam(equipossliga)
                isAddTeam = bool(input('Desea agregar otro equipo S(si) o Enter(no)'))
                
        elif op == 2:
            isAddFecha = True
            while isAddFecha:
                e.os.system = True
                e.Fechass(equipossliga)
                isAddFecha = bool(input('Desea agregar otras Fechas S(si) o Enter(no)'))
        elif op == 3:
            isRepport = True
            while isRepport:
                e.os.system = True
                opr = mr.menuReportes()
                if opr == 'A':
                    isGolesMax = True
                    while isGolesMax:
                        e.os.system = True
                        e.Reportess(equipossliga)
                        golesmaximos = e.Reportess(equipossliga)
                        print(f'El Equipo que mas goles anoto fue {golesmaximos}')
                        isGolesMax = bool(input('presiona Enter para continuar'))
                elif opr == 'B':
                    isPtsMax = True
                    while isPtsMax:
                        e.os.system = True
                        e.maxpts(equipossliga)
                        PtsMax = e.maxpts(equipossliga)
                        print(f'El Equipo que mas Puntos tuvo fue {PtsMax}')
                        isPtsMax = bool(input('presiona Enter para continuar'))
                elif opr == 'C':
                    isPtrMax = True
                    while isPtrMax:
                        e.os.system = True
                        e.maxptrs(equipossliga)
                        ptrsMax = e.maxptrs(equipossliga)
                        print(f'El Equipo que mas Partidos gano fue {ptrsMax}')
                        isPtrMax = bool(input('presiona Enter para continuar'))
                elif opr == 'D':
                    isGolto = True
                    while isGolto:
                        e.os.system = True
                        posicion = 5
                        e.sumagoles(equipossliga, posicion)
                        Goltol = e.sumagoles(equipossliga, posicion)
                        print(f'La cantidad de goles que se anotaron en total fue {Goltol}')
                        isGolto = bool(input('presiona Enter para continuar'))
                elif opr == 'E':  
                    isGolpro = True
                    while isGolpro:
                        posicion = 5
                        GolPro = e.promediogoles(equipossliga, posicion)
                        print(f'El promedio de goles anotados en el torneo fue {GolPro}')
                        isGolpro = bool(input('presiona Enter para continuar'))
                elif opr == 'F':
                    isRepport = False
            
        elif op == 4:
            isAppRunning = False
            
           
            







    
    