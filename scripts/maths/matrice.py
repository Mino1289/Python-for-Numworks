from random import randint


class Matrice:
    """
    Représente une Matrice dans Python, une liste de liste.
    """

    def __init__(self, M: list) -> None:
        self.value = M

    def __len__(self) -> int:
        return len(self.value)

    def __getitem__(self, i):
        return self.value[i]

    def __iter__(self):
        return self.value

    def __eq__(self, M: list) -> bool:
        if len(self.value) == len(M) and len(self.value[0]) == len(M[0]):
            for i in range(len(M)):
                for j in range(len(M[i])):
                    if self.value[i][j] != M[i][j]:
                        return False
            return True
        return False

    def __ne__(self, M: list) -> bool:
        if len(self.value) == len(M) and len(self.value[0]) == len(M[0]):
            for i in range(len(M)):
                for j in range(len(M[i])):
                    if self.value[i][j] != M[i][j]:
                        return True
            return False
        return True

    def __index__(self) -> list:
        return self.value

    def __str__(self) -> str:
        if self.value == []:
            return ""
        num_of_rows = len(self.value)
        num_of_cols = len(self.value[0])
        tp = ""
        for i in range(num_of_rows):
            row_to_print = ""
            for j in range(num_of_cols):
                value = self.value[i][j]
                row_to_print += str(value) + " "
            tp += row_to_print + "\n"
        return tp

    def __add__(self, M: list) -> list:
        if M == []:
            return self.value
        if len(self.value) != len(M) or len(self.value[0]) != len(M[0]):
            return self.value
        num_rows = len(self.value)
        num_cols = len(self.value[0])
        for i in range(num_rows):
            for j in range(num_cols):
                self.value[i][j] += M[i][j]
        return Matrice(self.value)

    def __sub__(self, M: list) -> list:
        """
        Soustrait deux matrices de même dimensions.
        L'argument doit être une liste de liste, représentant une matrice
        """
        if M == []:
            return self.value
        if len(self.value) != len(M) or len(self.value[0]) != len(M[0]):
            return self.value
        num_rows = len(self.value)
        num_cols = len(self.value[0])
        for i in range(num_rows):
            for j in range(num_cols):
                self.value[i][j] -= M[i][j]
        return Matrice(self.value)

    def __mul__(self, M: list) -> list:
        """
        Multiplie deux matrices, celle en argument,\n\n
        qui doit être une liste de liste, doit avoir le même nombre de ligne que la première a de colone.
        Renvoie une matrice de dimension (ligne de la première, colonne de celle en argument.)
        """
        if isinstance(M, list) or isinstance(M, Matrice):
            m = []
            if len(self.value[0]) != len(M):
                print("erreur")
                return m
            for i in range(len(self.value)):
                ligne = []
                for j in range(len(M[0])):
                    element = 0
                    for k in range(len(self.value[0])):
                        element += self.value[i][k] * M[k][j]
                    ligne.append(element)
                m.append(ligne)
            return Matrice(m)
        if isinstance(M, float) or isinstance(M, int):
            for i in range(len(self.value)):
                for j in range(len(self.value[i])):
                    self.value[i][j] *= M
            return Matrice(self.value)
        return Matrice(self.value)

    def __neg__(self) -> list:
        return Matrice(self.value)*(-1)

    def __pos__(self) -> list:
        return Matrice(self.value)*(1)

    def __abs__(self) -> list:
        x, y = len(self.value), len(self.value[0])
        for i in range(x):
            for j in range(y):
                self.value[i][j] = abs(self.value[i][j])
        return Matrice(self.value)

    def __int__(self) -> list:
        x, y = len(self.value), len(self.value[0])
        for i in range(x):
            for j in range(y):
                self.value[i][j] = int(self.value[i][j])
        return Matrice(self.value)

    def __float__(self) -> list:
        x, y = len(self.value), len(self.value[0])
        for i in range(x):
            for j in range(y):
                self.value[i][j] = float(self.value[i][j])
        return Matrice(self.value)

    def __round__(self, n=None) -> list:
        x, y = len(self.value), len(self.value[0])
        for i in range(x):
            for j in range(y):
                self.value[i][j] = round(self.value[i][j], n)
        return Matrice(self.value)

    def __complex__(self) -> list:
        x, y = len(self.value), len(self.value[0])
        for i in range(x):
            for j in range(y):
                self.value[i][j] = complex(self.value[i][j])
        return Matrice(self.value)

    def identity(self, n: int) -> list:
        """
        Renvoie la matrice identité d'ordre n.
        """
        M = []
        for i in range(n):
            L = []
            for j in range(n):
                if i == j:
                    L.append(1)
                else:
                    L.append(0)
            M.append(L)
        return Matrice(M)

    def is_squared(self) -> bool:
        """
        Renvoie un booléen, si la matrice est carrée.
        """
        return len(self.value) == len(self.value[0])

    def det(self) -> float:
        A = self.value
        n = len(A)
        if n == 0:
            return 1
        s = 0
        for j in range(n):
            s += A[0][j] * Matrice(A).cofacteur(0, j)
        return s

    def cofacteur(self, i: int, j: int) -> int:
        m = self.mineur(i, j)
        if (i + j) % 2 == 0:
            return m
        return -m

    def supprimer_ligne_colone(self, i: int, j: int) -> list:
        A = self.value
        n = len(A)
        rg = range(n-1)
        B = [[None for p in rg] for q in rg]
        for p in rg:
            for q in rg:
                B[p][q] = A[phi(p, i)][phi(q, j)]
        return B

    def mineur(self, i: int, j: int) -> int:
        A1 = self.supprimer_ligne_colone(i, j)
        return Matrice(A1).det()

    def comatrice(self) -> list:
        """
        Renvoie la comatrice de la matrice 
        """
        n = len(self.value)
        B = [[None for i in range(n)] for j in range(n)]
        for i in range(n):
            for j in range(n):
                B[i][j] = self.cofacteur(i, j)
        return Matrice(B)

    def transposee(self) -> list:
        """
        Renvoie la transposée de la Matrice.
        """
        m, n = len(self.value), len(self.value[0])
        B = [[None for i in range(n)] for j in range(m)]
        for i in range(n):
            for j in range(n):  # n ?
                B[i][j] = self.value[j][i]
        return Matrice(B)

    def inverse(self) -> list:
        """
        Renvoie l'inverse de la Matrice.
        """
        det = self.det()
        if det == 0:
            return None
        M = self.comatrice().transposee()*(1/det)
        return M

    def trace(self) -> float:
        """
        Renvoie la trace de la Matrice.
        """
        M = self.value
        return sum([M[i][j] for i in range(len(M)) for j in range(len(M[i])) if i == j])


def phi(p, i):
    if p < i:
        return p
    return p+1


def random_matrix(n):
    rg = range(n)
    return Matrice([[randint(-9, 9) for i in rg] for j in rg])
