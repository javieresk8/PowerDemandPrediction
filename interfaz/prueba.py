def crearMatriz():
    #Lista que es una matriz momentanea    
    matriz = []
    nFilas = 3
    nColumnas = 3
 
    for i in range(nFilas):
        matriz.append([0]*nColumnas)    
    for i in range(0,nFilas):       
        for j in range(0,nColumnas):            
            matriz[i][j] = '-'
    shape = (nFilas,nColumnas)
    return matriz, shape

def mostrarMatriz(matriz, shape):  
    x, y = shape   
    for i in range(0,x):
        for j in range(0,y):
            print(matriz[i][j],end="\t")
        print('')

def comprobarGanador(matriz, caracter):
    fin = False
    #por filas
    if (matriz[0][0] == caracter and matriz[0][1] == caracter and matriz[0][2]==caracter):
        fin = True
    if (matriz[1][0] == caracter and matriz[1][1] == caracter and matriz[1][2]==caracter):
        fin = True
    if (matriz[2][0] == caracter and matriz[2][1] == caracter and  matriz[2][2]==caracter):
        fin = True
    # por columnas
    if (matriz[0][0] == caracter and matriz[1][0] == caracter and  matriz[2][0] == caracter):
        fin = True
    if (matriz[0][1] == caracter and matriz[1][1] == caracter and  matriz[2][1] == caracter):
        fin = True
    if (matriz[0][2] == caracter and matriz[1][2] == caracter and  matriz[2][2] == caracter):
        fin = True
    #diagonales
    if (matriz[0][0] == caracter and matriz[1][1] == caracter and  matriz[2][2] == caracter):
        #print('diagonal 1')
        fin = True
    if (matriz[2][0] == caracter and matriz[1][1] == caracter and  matriz[0][2] == caracter):
        #print('diagonal 2')
        fin = True

    return fin

def main():
    matriz, dimensiones = crearMatriz()
    continuar = True   
    jugador1 = input('Caracter para el jugador 1: ')
    jugador2 = input('Caracter para el jugador 2: ')
    turno = int(input('¿Qué jugador empieza el juego [1] o [2]? '))
    while continuar==True:
        mostrarMatriz(matriz, dimensiones)
        print('Turno jugador ',turno)
        fila = int(input('Fila: '))
        columna = int(input('Columna: '))
        if turno == 1:
            matriz[fila-1][columna-1]=jugador1
            turno = 2
        else:
            matriz[fila-1][columna-1]=jugador2
            turno = 1
        if comprobarGanador(matriz, jugador1) == True:
            print('El jugador 1 ganó !!!')
            mostrarMatriz(matriz, dimensiones)
            continuar=False
        if comprobarGanador(matriz, jugador2) == True:
            print('El jugador 2 ganó !!!')
            mostrarMatriz(matriz,dimensiones)
            continuar=False

main()