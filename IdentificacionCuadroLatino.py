
def crearConjunto(mat): ## se crea el conjunto de todos los elementos de la tabla a partir de la primera fila
    set={}
    for i in range (1,len(mat[0])):
        set.setdefault(mat[0][i], False)
    return set

## se verifica por cada fila sí el elemento ya apareció una vez, 
## sí algun elemento no aparece ninguna vez es porque otro elemento se está repitiendo o
## algún elemento que no pertenece al conjunto está en la tabla  
def verificarFilas(mat,set): 
    try:
        for i in range(1, len(mat)):
            for j in range(1, len(mat[i])):
                ##print(mat[i][j]," ",set[mat[i][j]])
                if(set[mat[i][j]]== True):
                    return False
                set[mat[i][j]]= True
            for i in set:
                set[i]=[False, 0]
        return True
    except:
        return False

## se verifica por cada columna sí el elemento ya apareció una vez, 
## sí algun elemento no aparece ninguna vez es porque otro elemento se está repitiendo o
## algún elemento que no pertenece al conjunto está en la tabla
def verificarColumnas(mat, set):
    try:
        for j in range(1, len(mat)):
            for i in range(1, len(mat[j])):
                ##print(mat[i][j]," ",set[mat[i][j]])
                if(set[mat[i][j]]== True):
                    return False
                set[mat[i][j]]= True
            for i in set:
                set[i]=[False, 0]
        return True
    except:
        return False

def verificarLatino(mat, set):## se verifican filas y columnas
    cumpleFila = verificarFilas(mat, set)
    cumpleColumna = verificarColumnas(mat, set)
    return cumpleFila and cumpleColumna

def verificarFormato(mat):
    size=len(mat)
    for i in range(1, len(mat)):
        if(len(mat[i])!=size):
            return False
    return True

def buscarElementoEnPColumna(a, mat):
    for i in range(1, len(mat)):
        if(mat[i][0]==a):
            return i
    raise NameError('Tabla invalida')

def switchear(i, index, mat):
    last = mat[index]
    mat[index]= mat[i]
    mat[i]=last

def ordenarMatriz(mat):
    for i in range(1, len(mat)):
        if(mat[0][i]!=mat[i][0]):
            index = buscarElementoEnPColumna(mat[0][i],mat)
            switchear(i, index, mat)
    return mat

## se busca el elemento neutro, dado que la matriz se ordenó 
## poniendo los elemntos del conjunto en el mismo orden en fila y columna, 
## solo hace falta revisar la diagonal principal
def buscarNeutro(mat): 
    for i in range(1, len(mat)):
        if(mat[0][i]==mat[i][i] and mat[i][0]==mat[i][i]):
            return [mat[i][i], i]
    return False 


def verificarNeutro(neutro, mat):
    for i in range(1, len(mat)):
        if(mat[i][0]!=mat[i][neutro[1]]):
            return False
    return True

## se verifica con todas las triplas posibles (a*b)*c = a*(b*c), es O(n3)
## cada elemento se convierte en un indice del conjunto para operar más rapidamente
def verificarAsociatividad(matriz):
    n = len(matriz)  # Tamaño de la matriz

    for i in range(n):
        for j in range(n):
            for k in range(n):
                resultado1 = matriz[i][j] + (matriz[j][k] + matriz[i][k])
                resultado2 = (matriz[i][j] + matriz[i][k]) + matriz[j][k]
                if resultado1 != resultado2:
                    return False
    
    return True

     
##################################################################################
###################################################################################
## Programa 
###################################################################################

set = crearConjunto(matriz) ## se define el conjunto en base a el header de la tabla 
tieneFormato = verificarFormato(matriz) ## se verifica que sea cuadrada

if(tieneFormato):
    matriz = ordenarMatriz(matriz) ## se ordena para que cada elemento m[i][0] corresponda a cada m[0][i]
    esLatino = verificarLatino(matriz, set) ##se verifican filas y columnas, tambien que cada elemnto aparezca una sola vez y que sea una operación cerrada
    neutro = buscarNeutro(matriz) ## dado que se ordenó la matriz, el neutro debe estar en algun punto de la diagonal
    todosCumplenNeutro = verificarNeutro(neutro, matriz) ##no es del todo necesario ya que anteriormente se comprobo que todos deben tener neutro
    esAsociativo = verificarAsociatividad(matriz)
    ##print(esLatino, todosCumplenNeutro, neutro, esAsociativo)
    if(esLatino):
        print("es Cuadro Latino")
        if(esAsociativo and todosCumplenNeutro):
            print("es grupo")
        else: 
            print("no es grupo")
    else:
        print("no es Latino ni grupo")
else:
    print('tabla invalida')

