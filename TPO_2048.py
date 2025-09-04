import random,os

#Programa escrito y desarrollado por Agustin Monetti e Ignacio Blua 

def imp_mat(mat):
    '''Imprime la matriz con un formato de forma que cada elemento se encuentre dentro de
un cuadrado, de manera centrada'''
    
    print("-"*6*len(mat[0]))
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            print(f"|{mat[i][j]:^4}|",end="")
        print()
        print("-"*6*len(mat[i]))


def rellenar(mat):
    '''Busca algun espacio vacio en la matriz, y en caso de haberlo, lo rellena con o un 2 el
90% de las veces, o un 4 el 10% de las veces'''
    
    probab = (2,)*9 + (4,)
    cols = [i[0] for i in enumerate(mat) if 0 in i[1]]
    
    if len(cols) > 0:
        a = random.choice(cols)
        b = random.choice([i[0] for i in enumerate(mat[a]) if i[1] == 0])
        
        mat[a][b] = random.choice(probab)

#________________________________________________________________________

def mov_izq(mat):
    '''Realiza todos los movimientos posibles hacia la izquierda en la matriz,
 y devuelve la suma de puntos obtenidos con dicho movimiento'''
    
    puntos = 0
    for i in range(len(mat)):
        sumados = []
        for j in range(1,len(mat)):
            if mat[i][j] == 0:
                continue
            for k in range(j,0,-1):
                if mat[i][k] == mat[i][k-1] and k not in sumados and k-1 not in sumados:
                    mat[i][k-1] += mat[i][k]
                    mat[i][k] = 0
                    sumados.append(k-1)
                    puntos += mat[i][k-1]
                    
                elif mat[i][k-1] == 0:
                    mat[i][k-1] = mat[i][k]
                    mat[i][k] = 0
                    if k in sumados:
                        sumados[-1] += -1
                else:
                    break
    
    return puntos

def mov_der(mat):
    '''Realiza todos los movimientos posibles hacia la derecha en la matriz,
 y devuelve la suma de puntos obtenidos con dicho movimiento'''
    
    puntos = 0
    for i in range(len(mat)):
        sumados = []
        for j in range(len(mat[i])-2,-1,-1):
            if mat[i][j] == 0:
                continue
            for k in range(j,len(mat[i])-1):
                if mat[i][k] == mat[i][k+1] and k not in sumados and k+1 not in sumados:
                    mat[i][k+1] += mat[i][k]
                    mat[i][k] = 0
                    sumados.append(k+1)
                    puntos += mat[i][k+1]
                elif mat[i][k+1] == 0:
                    mat[i][k+1] = mat[i][k]
                    mat[i][k] = 0
                    if k in sumados:
                        sumados[-1] += 1
                else:
                    break
    
    return puntos
                
def mov_abj(mat):
    '''Realiza todos los movimientos posibles hacia abajo en la matriz,
 y devuelve la suma de puntos obtenidos con dicho movimiento'''
    
    puntos = 0
    for i in range(len(mat[0])):
        sumados = []
        for j in range(len(mat)-2,-1,-1):
            if mat[j][i] == 0:
                continue
            for k in range(j,len(mat)-1):
                if mat[k][i] == mat[k+1][i] and k not in sumados and k+1 not in sumados:
                    mat[k+1][i] += mat[k][i]
                    mat[k][i] = 0
                    sumados.append(k+1)
                    puntos += mat[k+1][i]
                elif mat[k+1][i] == 0:
                    mat[k+1][i] = mat[k][i]
                    mat[k][i] = 0
                    if k in sumados:
                        sumados[-1] +=1
                else:
                    break
    
    return puntos

                
def mov_arr(mat):
    '''Realiza todos los movimientos posibles hacia arriba en la matriz,
 y devuelve la suma de puntos obtenidos con dicho movimiento'''
    
    puntos = 0
    for i in range(len(mat[0])):
        sumados = []
        for j in range(1,len(mat)):
            if mat[j][i] == 0:
                continue
            for k in range(j,0,-1):
                if mat[k][i] == mat[k-1][i] and k not in sumados and k-1 not in sumados:
                    mat[k-1][i] += mat[k][i]
                    mat[k][i] = 0
                    sumados.append(k-1)
                    puntos += mat[k-1][i]
                elif mat[k-1][i] == 0:
                    mat[k-1][i] = mat[k][i]
                    mat[k][i] = 0
                    if k in sumados:
                        sumados[-1] += -1
                else:
                    break
    
    return puntos

#______________________________________________________________________


def leer_usuario(usuario):
    ''' Devuelve una lista con todos los datos de un usuario en particular,
en caso de no existir tal jugador, se devuelve una lista vacia'''
    
    try:
        arc = open("player_log.txt","rt")
    except FileNotFoundError:
        return ()
    
    registro = "registro"
    while registro != "":
        registro = arc.readline()[:-1]
        lis = registro.split(";")
        if lis[0] == usuario:
            tup = (lis[0],int(lis[1]),int(lis[2]),lis[3].split(","))
            for i in range(len(tup[-1])):
                tup[-1][i] = int(tup[-1][i])
            break
    else:
        tup = ()
    
    arc.close()
    return tup

def reescribir_archivo(t_cambios):
    '''Toma un tuple con datos, y los actualiza el archivo principal del juego'''
    
    se_encontro = False
    
    for i in range(len(t_cambios[-1])):
        t_cambios[-1][i] = str(t_cambios[-1][i])
    t_cambios = (t_cambios[0],str(t_cambios[1]),str(t_cambios[2]),",".join(t_cambios[-1]))
    cambios = ";".join(t_cambios)+"\n"

    try:
        arc_lec = open("player_log.txt","rt")
        arc_esc = open("player_log_TEMP.txt","wt")
        registro = arc_lec.readline()
        
        while registro != "":
            
            if registro.split(";")[0] == t_cambios[0]:
                arc_esc.write(cambios)
                se_encontro = True
            else:
                arc_esc.write(registro)
            
            registro = arc_lec.readline()
            
        
        if not se_encontro:
            arc_esc.write(cambios)
            
        arc_lec.close()
        arc_esc.close()
            
    except FileNotFoundError:
        arc_esc = open("player_log.txt","wt")
        arc_esc.write(cambios)
        arc_esc.close()
     
    else:
        os.remove("player_log.txt")
        os.rename("player_log_TEMP.txt","player_log.txt")
        
        
#______________________________________________________________

def de_linea_a_mat(lis,mat):
    '''Carga una matriz a partir de una lista'''
    for i in range(len(lis)):
        mat[i//len(mat)][i%len(mat)] = lis[i]
        
def de_mat_a_linea(lis,mat):
    '''Guarda una matriz en forma de lista'''
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            lis[i*len(mat)+j] = mat[i][j]

#________________________________________________

def comp_izq_r(lis,k):
    '''comprueba si algun elemento de la lista se podria mover/ combinar hacia la izquierda'''
    
    se_puede = False
    if k != 0 and not se_puede:
        if lis[k-1] == lis[k] and lis[k]!=0:
            return True
        elif lis[k-1]== 0 and lis[k]!=0:
            return True
        
        se_puede = comp_izq_r(lis,k-1)
    
    return se_puede

def col_a_fil(mat,j):
    '''devuelve una lista a partir de una columna j de una matriz '''
    
    lis = [0]*len(mat)
    for i in range(len(mat)):
        lis[i] = mat[i][j]
    return lis

def ver_izq(mat):
    '''Verifica que haya por lo menos un movimiento valido hacia la
izquierda en la matriz'''
    
    es_movible = False
    for i in mat:
        if comp_izq_r(i,len(i)-1):
            es_movible = True
            break
    
    return es_movible

def ver_der(mat):
    '''Verifica que haya por lo menos un movimiento valido hacia la
derecha en la matriz'''
    
    es_movible = False
    for i in mat:
        fil = i.copy()
        fil.reverse()
        if comp_izq_r(fil,len(i)-1):
            es_movible = True
            break
    
    return es_movible

def ver_arr(mat):
    '''Verifica que haya por lo menos un movimiento valido hacia
arriba en la matriz'''
    
    es_movible = False
    for i in range(len(mat[0])):
        fil = col_a_fil(mat,i)
        if comp_izq_r(fil,len(fil)-1):
            es_movible = True
            break
    
    return es_movible

def ver_abj(mat):
    '''Verifica que haya por lo menos un movimiento valido hacia
abajo en la matriz'''
    
    es_movible = False
    for i in range(len(mat[0])):
        fil = col_a_fil(mat,i)
        fil.reverse()
        if comp_izq_r(fil,len(fil)-1):
            es_movible = True
            break
    
    return es_movible


#_____________________________________________________

movs = {"izquierda":mov_izq,"derecha":mov_der,"abajo":mov_abj,"arriba":mov_arr}
vers = {"izquierda":ver_izq,"derecha":ver_der,"abajo":ver_abj,"arriba":ver_arr}
direcs = set(movs.keys())
matriz = [[0]*4 for i in range(4)]
puntos = 0
h_puntos = 0

#Comienza main
print("\n" + "="*50)
print("J U E G O   2 0 4 8  🎮")
print("="*50)
print()
usuario = input("Por favor, ingrese su nombre de usuario: ")
datos = leer_usuario(usuario)

if len(datos) == 0:
    print(f"NO se ha encontrado ningun usuario con ese nombre. Un nuevo usuario ha sido creado con el nombre {usuario}")
    datos = (usuario,0,0,[0]*16)
    rellenar(matriz)
else:
    if input("Desea continuar su ultima partida? <S/N>:").lower() == "s":
        de_linea_a_mat(datos[-1],matriz)
        puntos = datos[-2]
    else:
        rellenar(matriz)
    h_puntos = datos[1]

#---------------------------------------------------------------
es_posible = True
es_ganado = False

while es_posible and not es_ganado:
    print()
    print(f"MEJOR puntaje: {h_puntos}")
    print(f"Puntaje ACTUAL: {puntos}")
    imp_mat(matriz)
    
    
    dire = input("Ingrese una direccion para mover <izquierda/derecha/arriba/abajo> o ingrese <salir> para salir: ").lower()
    if dire == "salir":
        break
    
    elif dire in direcs:
        if vers[dire](matriz):
            puntos += movs[dire](matriz)
            h_puntos = puntos if puntos > h_puntos else h_puntos
            rellenar(matriz)
        else:
            print()
            print("AVISO: NO se puede mover en dicha direccion, intente otra")
    else:
        print()
        print("-"*46)
        print("ERROR: Por favor, ingrese una direccion VALIDA")
        print("-"*46 + "\n")
        continue
    
    
    for i in matriz:
        es_ganado = True if 2048 in i else False
    
    es_posible = False
    
    for i in direcs:
        if vers[i](matriz):
            es_posible = True
            break


if es_ganado or not es_posible:
    if es_ganado:
        print("\n" + "="*50 )
        print("¡FELICITACIONES! ")
        print("Has llegado a 2048 y ganado esta partida")
        print("="*50 )
    else:
        print("\n" + "="*50)
        print("GAME OVER")
        print("No hay más movimientos posibles y consecuentemente esta partida se encuentra perdida y finalizada")

    matriz = [[0]*4 for i in range(4)]
    rellenar(matriz)
    puntos = 0


datos = (usuario, h_puntos, puntos, datos[-1])
de_mat_a_linea(datos[-1],matriz)
reescribir_archivo(datos)



#FORMATO ARCHIVO:
#usuario;putaje_maximo;puntaje_actual;mat[0],mat[1],...,mat[n]
