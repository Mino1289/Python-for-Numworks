from random import randint
from time import sleep


def create_board():
    return [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


def print_board(board):
    if board == []:
        print("Empty Matrix")
    num_of_rows = len(board)
    num_of_cols = len(board[0])

    print(">x|1 2 3|")
    for i in range(num_of_rows):
        print("--|------")
        row_to_print = str(i+1) + " |"
        for j in range(num_of_cols):
            value = board[i][j] if board[i][j] != 0 else " "
            row_to_print += str(value) + "|"
        print(row_to_print)
    print("--|------")


def is_win(board):
    for i in range(len(board)):
        # on vérifie chaque ligne
        if board[i].count("x") == 3:
            return True, "x"
        for j in range(len(board[i])):
            L = []
            for k in range(len(board)):
                L.append(board[k][j])
                if L.count("x") == 3:
                    return True, 'x'
        if board[0][0] == board[1][1] == board[2][2] and board[0][0] != 0 and board[1][1] != 0 and board[2][2] != 0:
            if board[1][1] == "x":
                return True, "x"
            else:
                return True, "o"
        if board[0][2] == board[1][1] == board[2][0] and board[0][2] != 0 and board[1][1] != 0 and board[2][0] != 0:
            if board[1][1] == "x":
                return True, "x"
            else:
                return True, "o"

    for i in range(len(board)):
        # on vérifie chaque ligne
        if board[i].count("o") == 3:
            return True, 'o'
        for j in range(len(board[i])):
            L = []
            for k in range(len(board)):
                L.append(board[k][j])
                if L.count("o") == 3:
                    return True, 'o'
    return False


def find_mt(board):
    for x in range(3):
        for y in range(3):
            if board[x][y] == 0:
                return [x, y]
    return None


def ia(board):
    x = 0
    for i in range(len(board)):
        x += board[i].count(0)
    x = 9-x
    if x == 1 and board[1][1] == 0:
        board[1][1] = "o"
        return board

    for k in board:  # test de la ligne
        # attaque
        if k.count("o") == 2 and k.count(0) >= 1:
            board[board.index(k)][k.index(0)] = "o"
            return board
    for k in board:
        # defense
        if k.count("x") == 2 and k.count(0) >= 1:
            board[board.index(k)][k.index(0)] = "o"
            return board

    for x in range(len(board[0])):  # ligne
        L = []  # on constitue une liste de la colonne
        for y in range(len(board)):  # colonne
            L.append(board[y][x])
        # attaque
        if L.count("o") == 2 and L.count(0) >= 1:
            board[L.index(0)][x] = "o"
            return board

    for x in range(len(board[0])):
        L = []
        for y in range(len(board)):
            L.append(board[y][x])
        # defense
        if L.count("x") == 2 and L.count(0) >= 1:
            board[L.index(0)][x] = "o"
            return board

    # diagonale :
    # normale haut gauche => bas droit
    L = [board[0][0], board[1][1], board[2][2]]
    if L.count("o") == 2 and L.count(0) >= 1:
        board[L.index(0)][L.index(0)] = "o"
        return board
    if L.count("x") == 2 and L.count(0) >= 1:
        board[L.index(0)][L.index(0)] = "o"
        return board

    # opposé haut droit => bas gauche
    L = [board[0][2], board[1][1], board[2][0]]
    if L.count("o") == 2 and L.count(0) >= 1:
        if L[0] == 0:
            board[0][2] = "o"
            return board
        elif L[1] == 0:
            board[1][1] = "o"
            return board
        else:
            board[2][0] = "o"
            return board
    if L.count("x") == 2 and L.count(0) >= 1:
        if L[0] == 0:
            board[0][2] = "o"
            return board
        elif L[1] == 0:
            board[1][1] = "o"
            return board
        else:
            board[2][0] = "o"
            return board
    # Stratégie: attaque
    for k in range(len(board)):
        for i in range(len(board[k])):
            L = []
            for j in range(len(board)):
                L.append(board[j][i])
            for j in range(len(board)):
                if board[k].count(0) == 2 and board[k].count("o") == 1 and L.count(0) == 2 and L.count("o") == 1:
                    # trouver l'intersection en espérant que ce soit pas deja coché
                    for x in range(len(L)):
                        if board[j][i] == 0 and board[j][i] == L[x] and board[j].count("o") == 1 and board[j].count("x") == 0:
                            board[j][i] = "o"
                            return board
    # Stratégie : défense
    for k in range(len(board)):
        for i in range(len(board[k])):
            L = []
            for j in range(len(board)):
                L.append(board[j][i])
            for j in range(len(board)):
                if board[k].count(0) == 2 and board[k].count("x") == 1 and L.count(0) == 2 and L.count("x") == 1:
                    # trouver l'intersection en espérant que ce soit pas deja coché
                    for x in range(len(L)):
                        if board[j][i] == 0 and board[j][i] == L[x] and board[j].count("x") == 1 and board[j].count("o") == 0:
                            board[j][i] = "o"
                            return board

    if find_mt(board) is not None:
        board[find_mt(board)[0]][find_mt(board)[1]] = "o"
        return board
    else:
        return board


def play():
    tour = 4
    board = create_board()
    if randint(0, 1) == 1:
        print("Vous commencez !")
        tour += 1
    else:
        board[randint(0, 2)][randint(0, 2)] = "o"
    print("Vous placez les x. Vous devez \ndonner la position de votre croix")
    print_board(board)
    for k in range(tour):
        if is_win(board):
            msg = "\nTu as gagné !" if is_win(
                board)[1] == "x" else "\nLa machine a gagné, tu as perdu."
            print(msg)
            return
        x = int(input("x = "))
        y = int(input("y = "))
        print("\n")
        if board[y-1][x-1] == 0:
            board[y-1][x-1] = "x"
        else:
            while board[y-1][x-1] != 0:
                print("\nCette case est deja occupé\nChoisissez une autre\n")
                x = int(input("x = "))
                y = int(input("y = "))
                print("\n")
            else:
                board[y-1][x-1] = "x"

        print_board(board)
        sleep(1.5)

        if is_win(board):
            msg = "\nTu as gagné !" if is_win(
                board)[1] == "x" else "\nLa machine a gagné, tu as perdu."
            print(msg)
            return
        # tour de la machine
        if find_mt(board) is None:
            print("Fini, pas de gagnant :(")
            break
        board = ia(board)
        print("\nLa machine a joué :\n")
        print_board(board)
        if k+1 == tour:
            if is_win(board):
                msg = "\nTu as gagné !" if is_win(
                    board)[1] == "x" else "\nLa machine a gagné, tu as perdu."
                break
            else:
                print("Fini, pas de gagnant :(")
            break


play()


grille = [
    ["o", "x", 0],
    ["x", 0, 0],
    [0, 0, 0]
]

# print_board(grille)
# print("\n")
# print_board(ia(grille))
