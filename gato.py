

import os


def dibujar_tablero(tablero, jugador):
    os.system('clear')
    print('=============')
    print('Juego de gato!')
    print('=============')
    print('')
    
    print(" %s | %s | %s " % (tablero[0][0],tablero[0][1],tablero[0][2]))
    print("---+---+---")
    print(" %s | %s | %s " % (tablero[1][0],tablero[1][1],tablero[1][2]))
    print("---+---+---")
    print(" %s | %s | %s " % (tablero[2][0],tablero[2][1],tablero[2][2]))
    print('')
    print('=============')
    print('')
    print(f"Es el turno del Jugador {jugador}")

    

def movimiento(jugador, fila, columna, tablero):
    # print(jugador)
    # print(f"Movimiento fila = {fila} columna = {columna}")
    tablero[fila][columna] = jugador

def cambiar_jugador(jugador):     
    if jugador == 'X': 
        jugador = 'O'
    else:
        jugador = 'X'
        
    return jugador

def validar_ganador_horizontal(ganador, tablero):
    # Revisar lineas horizontales
    for fila in tablero:
       # print(fila)
        if (fila[0] == fila[1] == fila[2] != ' '):
            ganador = True;
    return ganador
def validar_ganador_vertical(ganador, tablero):
    for columna in range(3):
        if (tablero[0][columna] == tablero[1][columna] == tablero[2][columna] != ' '):
            ganador = True
    return ganador  
def validar_ganador_diagonal(ganador, tablero):
    # print(tablero[0][0], tablero[1][1], tablero[2][2])

    if(tablero[0][0] == tablero[1][1] == tablero[2][2] != ' '):
        ganador = True

    if ganador == False: 
        # print(tablero[2][0], tablero[1][1], tablero[0][2])
        ganador = (tablero[2][0] == tablero[1][1] == tablero[0][2] != ' ')
        
    return ganador

def validar_ganador(ganador, tablero):
    resultado = False

    if (validar_ganador_horizontal(ganador, tablero)):
        resultado = True
    elif(validar_ganador_vertical(ganador, tablero)):
        resultado = True
    elif(validar_ganador_diagonal(ganador, tablero)):
        resultado = True
    
    print('validar_ganador ', resultado)
    return resultado

def main():    
    
    tablero = [
        [' ',' ',' '],
        [' ',' ',' '],
        [' ',' ',' ']
    ]

    ganador = False
    jugador = 'X'
    
    while not ganador:
        dibujar_tablero(tablero, jugador)

        fila = input('Seleccione la fila: ')
        columna = input('Seleccione la columna: ')

        if (fila.isdecimal() and columna.isdecimal()):
            fila = int(fila)
            columna = int(columna)        
 
            movimiento(jugador, fila, columna, tablero)

            ganador = validar_ganador(ganador, tablero)
            if not ganador :
                jugador = cambiar_jugador(jugador)
    
    dibujar_tablero(tablero, jugador)    
    print(f" ############## El gadador es el jugador : {jugador}  ##############")

main()
