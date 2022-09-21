"""
Este es un programa que nos permitirá jugar en familia el juego conocido en Colombia como Triqui,
En este juego se debe seleccionar con números del 1 al 9 las casillas dónde se quiere poner
la "X" o la "O" dependiendo del turno de jugador que escojas.
"""

"Defino mis variables globales"
espacio_marcado="Ese espacio ya está marcado"
tablero=[" " for i in range(9)]

"Creación de función para creación del tablero"
def print_tablero():
    fila1=f"|  {tablero[0]}  |  {tablero[1]}  |  {tablero[2]}  |"
    fila2=f"|  {tablero[3]}  |  {tablero[4]}  |  {tablero[5]}  |"
    fila3=f"|  {tablero[6]}  |  {tablero[7]}  |  {tablero[8]}  |"

    print("_"*19)
    print()
    print(fila1)
    print("_"*19)
    print()
    print(fila2)
    print("_"*19)
    print()
    print(fila3)
    print("_"*19)

"Creación de función para que los jugadores escojan las casilla y poder empezar a jugar"
def seleccion_movimiento(simbolo):

    if simbolo== "X":
        numero=1
    elif simbolo== "O":
        numero=2
    print(f"Es el turno del jugador número {numero}, por favor selecciona tu casilla")

    seleccion=int((input("Ingrese el lugar de ubicación de su movimiento (Número del 1-9): ")).strip())

    if tablero[seleccion-1]==" ":
        tablero[seleccion-1]=simbolo
    else:
        print()
        print(espacio_marcado)
        return True

"Función para seleccionar el ganador en caso de que lo haya."
def seleccion_ganador(simbolo):
    if (tablero[0] == simbolo and tablero[1] == simbolo and tablero[2] == simbolo) or \
        (tablero[3] == simbolo and tablero[4] == simbolo and tablero[5] == simbolo) or \
        (tablero[6] == simbolo and tablero[7] == simbolo and tablero[8] == simbolo) or \
        (tablero[0] == simbolo and tablero[3] == simbolo and tablero[6] == simbolo) or \
        (tablero[1] == simbolo and tablero[4] == simbolo and tablero[7] == simbolo) or \
        (tablero[2] == simbolo and tablero[5] == simbolo and tablero[8] == simbolo) or \
        (tablero[0] == simbolo and tablero[4] == simbolo and tablero[8] == simbolo) or \
        (tablero[2] == simbolo and tablero[4] == simbolo and tablero[6] == simbolo) :
        return True
    else:
        return False

"Función para en caso de no haber ganador se muestre el empate"
def empate():
    sin_espacio=" "
    if sin_espacio not in tablero:
        return True
    else:
        return False
     
        

if __name__=="__main__":
    while True:
        print_tablero()

        seleccion_movimiento("X")
        if espacio_marcado==True:
            seleccion_movimiento("X")

        print_tablero()
        if seleccion_ganador("X"):
            print("El ganador de la partida es X")
            break
        elif empate():
            print("El resultado es un empate")
            break
        
        seleccion_movimiento("O")
        if espacio_marcado==True:
            seleccion_movimiento("O")
       
        print_tablero()
        if seleccion_ganador("X"):
            print("El ganador de la partida es X")
            break
        elif empate():
            print("El resultado es un empate")
            break