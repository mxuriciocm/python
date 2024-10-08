def free(row, col, n):
    """ Determina si la casilla rowxcol está libre de ataques.

    @param row: Fila
    @param col: Columna
    @return: True si la casilla está libre de ataques por otras reinas.
    """
    for i in range(n):
        if tablero[row][i] == 'R' or tablero[i][col] == 'R':
            return False

    if row <= col:
        c = col - row
        r = 0
    else:
        r = row - col
        c = 0
    while c < n and r < n:
        if tablero[r][c] == 'R':
            return False
        r += 1
        c += 1

    if row <= col:
        r = 0
        c = col + row
        if c > n-1:
            r = c - (n-1)
            c = n-1
    else:
        c = n-1
        r = row - ((n-1) - col)

    while c >= 0 and r < n:
        if tablero[r][c] == 'R':
            return False
        r += 1
        c -= 1

    return True

def agregar_reina(n,m):
    """ Agrega n reinas al tablero.

    @param: n El número de reinas a agregar
    @return True si se pudo agregar las reinas requeridas
    """
    if m < 1:
        return True

    for idx_row in range(n):
        for idx_col in range(n):
            if free(idx_row, idx_col, n):
                tablero[idx_row][idx_col] = 'R'
                if agregar_reina(n,m-1):
                    return True
                else:
                    tablero[idx_row][idx_col] = '_'

    return False

n= int(input("DIGITE NUMERO DE REINAS: "))
m=n
tablero = []
for i in range(n):
    tablero.append(['_'] * n)
agregar_reina(n,m)
for row in tablero:
    print(*row)

# usar un método recursivo con backtracking.
# El método recursivo es el siguiente: Se recibe el tablero y se pide poner n reinas. Se busca secuencialmente una casilla desocupada, no amenazada por otras reinas. 
# Si se encuentra, se pone una reina y luego se invoca recursivamente la misma función para poner n-1 reinas.
# El backtracking aparece cuando no se logran colocar otra reinas. En tal caso, se deshace la última reina y se busca otra casilla más adelante,
#  desocupada, reintentando colocarla y comprobar si así se logran las ocho reinas. Si finalmente no se encuentra ninguna casilla apropiada,
#  se retrocede un nivel y se prueba a reubicar la reina anterior, y asi sucesivamente.
#La función free(row, col) chequea que la casilla no este afectada por alguna otra reina.