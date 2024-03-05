lstequipos = list

def AddTeam(lstequipos : list):
    nombre = input('ingrese el nombre del equipo : ')
    lstequipos.append([nombre, '0', '0', '0', '0', '0', '0', '0'])
    
    
    
    
    
def Fechass(lstequipos : list):
    partidosga = 0
    partidosper = 0
    partidosemp = 0
    Totalpts = 0
    GolesFavtol = 0
    GolesContol = 0
    nombre2 = input('ingrese el nombre del equipo del cual quiere ingresar las fechas : ')
    partidos2 = int(input('ingrese el numero de Fechas que jugo el equipo : '))
    
    
    if nombre2 == lstequipos[0]:
        
print(lstequipos[0])