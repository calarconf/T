
def crearConjunto(mat): 
    set={}
    for i in range (1,len(mat[0])):
        set.setdefault(mat[0][i], False)
    return set


def verificarFilas(mat,set): 
    try:
        for i in range(1, len(mat)):
            for j in range(1, len(mat[i])):
                if(set[mat[i][j]]== True):
                    return False
                set[mat[i][j]]= True
            for i in set:
                set[i]=[False, 0]
        return True
    except:
        return False


def verificarColumnas(mat, set):
    try:
        for j in range(1, len(mat)):
            for i in range(1, len(mat[j])):
                if(set[mat[i][j]]== True):
                    return False
                set[mat[i][j]]= True
            for i in set:
                set[i]=[False, 0]
        return True
    except:
        return False

def verificarLatino(mat, set):
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

def verificarAsociatividad(mat): 
    conjunto = []
    dic = {}

    for i in range(1,len(mat[0])):
        conjunto.append(mat[0][i])
        dic.setdefault(mat[0][i], i)
    for i in range(1,len(mat)):
        for j in range(1, len(mat[i])):
            mat[i][j]=dic[mat[i][j]]

    for i in range(1, len(conjunto)+1):
        for j in range(1, len(conjunto)+1):
            for k in range(1, len(conjunto)+1):
                if(mat[mat[i][j]][k]!=mat[i][mat[j][k]]):
                    return False
    return True         
     
matriz = [[  0,'a','f1','f2','f3','f4','f5'], 
          ['a','a','f1','f2','f3','f4','f5'],
          ['f1','f1','a','f3','f4','f5','f2'],
          ['f2','f2','f3','a','f5','f1','f4'],
          ['f3','f3','f4','f5','a','f2','f1'],
          ['f4','f4','f5','f1','f2','a','f3'],
          ['f5','f5','f2','f4','f1','f3','a']] 

set = crearConjunto(matriz)
tieneFormato = verificarFormato(matriz) 

if(tieneFormato):
    matriz = ordenarMatriz(matriz) 
    esLatino = verificarLatino(matriz, set) 
    neutro = buscarNeutro(matriz) 
    todosCumplenNeutro = verificarNeutro(neutro, matriz) 
    esAsociativo = verificarAsociatividad(matriz)
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

