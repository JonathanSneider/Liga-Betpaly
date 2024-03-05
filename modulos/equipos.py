import os
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
    
         
    
    for i in range(0,partidos2,1):

        Local = input(f'ingrese el equipo que jugo de local en la fecha {i+1} : ')
        Visitante = input('ingrese el equipo que jugo de visitante : ')
        GolesFav = int(input(f'ingrese lo goles que metio el equipo {nombre2} : '))
        GolesCon = int(input('ingrese los goles que metio el otro equipo : '))
        
        GolesFavtol =  GolesFavtol + GolesFav
        GolesContol = GolesContol + GolesCon
        
        
        
        if (GolesFav > GolesCon):
            partidosga = partidosga + 1
            
        elif (GolesFav < GolesCon):
            partidosper = partidosper + 1
            
        elif (GolesFav == GolesCon):
            partidosemp = partidosemp + 1
            
        if (GolesFav > GolesCon):
            Totalpts = Totalpts + 3
            
        elif (GolesFav < GolesCon):
            Totalpts = Totalpts + 0
            
        elif (GolesFav == GolesCon):
            Totalpts = Totalpts + 1
            
    for idx,item in enumerate(lstequipos):
        if (nombre2 in item):
            lstequipos[idx][1] = partidos2
            lstequipos[idx][2] = partidosga
            lstequipos[idx][3] = partidosper
            lstequipos[idx][4] = partidosemp
            lstequipos[idx][5] = GolesFavtol
            lstequipos[idx][6] = GolesContol
            lstequipos[idx][7] = Totalpts
            
def Reportess(lstequipos):
    maxGolesFav = float('-inf')
    lista_con_maximo = None  
    
    for lista in lstequipos:
        
        valor_posicion = lista[5]
        
        
        try:
            valor_posicion = int(valor_posicion)
            
            
            if valor_posicion > maxGolesFav:
                maxGolesFav = valor_posicion
                lista_con_maximo = lista  
        except ValueError:
            
            pass
            
    return lista_con_maximo[0]

def promediogoles(lstequipos, posicion):
    suma_total = 0
    cantidadL = 0
    resultadooo = 0
    
    for lista in lstequipos:
        try:
            vposicion = int(lista[posicion])
            suma_total += vposicion
            cantidadL += 1
        except (IndexError, ValueError):
            pass
    
    resultadooo = suma_total / cantidadL    
    return resultadooo

def maxpts(lstequipos):
    maxGolesFav = float('-inf')
    lista_con_maximo = None  
    
    for lista in lstequipos:
        
        valor_posicion = lista[7]
        
        
        try:
            valor_posicion = int(valor_posicion)
            
            
            if valor_posicion > maxGolesFav:
                maxGolesFav = valor_posicion
                lista_con_maximo = lista  
        except ValueError:
            
            pass
            
    return lista_con_maximo[0]

def maxptrs(lstequipos):
    maxGolesFav = float('-inf')
    lista_con_maximo = None  
    
    for lista in lstequipos:
        
        valor_posicion = lista[2]
        
        
        try:
            valor_posicion = int(valor_posicion)
            
            
            if valor_posicion > maxGolesFav:
                maxGolesFav = valor_posicion
                lista_con_maximo = lista  
        except ValueError:
            
            pass
            
    return lista_con_maximo[0]

def sumagoles(lstequipos, posicion):
    suma_total = 0
    
    for lista in lstequipos:
        try:
            valor_posicion = int(lista[posicion])
            suma_total += valor_posicion
        except (IndexError, ValueError):
            pass
            
    return suma_total




             
    
            
    
        
    
                
    
            
  
                
        
    
    
    
         
    
    
        
        
    
    
    

    
   
