from random import randint


class Matrice:
    """
    Représente une Matrice dans Python, une liste de liste.
    """

    def __init__(self, M: list) -> None:
        self.value = M

    def __repr__(self):
        return str(self)

    def __len__(self) -> int:
        return len(self.value)

    def __getitem__(self, i):
        return self.value[i]

    def __iter__(self):
        return iter(self.value)

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

    def __str__(self) -> str:
        if self.value == []:
            return ""
        num_of_rows = len(self)
        num_of_cols = len(self[0])
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
        return self

    def __sub__(self, M: list) -> list:
        if M == []:
            return self.value
        if len(self.value) != len(M) or len(self.value[0]) != len(M[0]):
            return self.value
        num_rows = len(self.value)
        num_cols = len(self.value[0])
        for i in range(num_rows):
            for j in range(num_cols):
                self.value[i][j] -= M[i][j]
        return self

    def __mul__(self, M: list) -> list:
        if isinstance(M, list) or isinstance(M, Matrice):
            m = []
            if len(self.value[0]) != len(M):
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
        if isinstance(M, float) or isinstance(M, int) or isinstance(M, complex):
            n, m = len(self), len(self[0])
            B = [[None for _ in range(m)] for _ in range(n)]
            for i in range(n):
                for j in range(m):
                    B[i][j] = self[i][j] * M
            return Matrice(B)
        return self

    def __neg__(self) -> list:
        return self*(-1)

    def __pos__(self) -> list:
        return self

    def __abs__(self) -> list:
        x, y = len(self.value), len(self.value[0])
        for i in range(x):
            for j in range(y):
                self.value[i][j] = abs(self.value[i][j])
        return self

    def __round__(self, n=0) -> list:
        x, y = len(self.value), len(self.value[0])
        for i in range(x):
            for j in range(y):
                self.value[i][j] = round(self.value[i][j], n)
        return self

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

    def determinant(self) -> float:
        n = len(self)
        if n == 0:
            return 1
        s = 0
        for j in range(n):
            s += self[0][j] * self.cofacteur(0, j)
        return s

    def cofacteur(self, i: int, j: int) -> int:
        m = self.mineur(i, j)
        if (i + j) % 2 == 0:
            return m
        return -m

    def supprimer_ligne_colone(self, i: int, j: int) -> list:
        n = len(self)
        rg = range(n-1)
        B = [[None for _ in rg] for _ in rg]
        for p in rg:
            for q in rg:
                B[p][q] = self[phi(p, i)][phi(q, j)]
        return Matrice(B)

    def mineur(self, i: int, j: int) -> int:
        A1 = self.supprimer_ligne_colone(i, j)
        return A1.determinant()

    def comatrice(self) -> list:
        """
        Renvoie la comatrice de la matrice 
        """
        if not self.is_squared():
            return None
        n = len(self.value)
        B = [[None for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                B[i][j] = self.cofacteur(i, j)
        return Matrice(B)

    def transposee(self) -> list:
        """
        Renvoie la transposée de la Matrice.
        """
        m, n = len(self.value), len(self.value[0])
        B = [[None for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                B[i][j] = self.value[j][i]
        return Matrice(B)

    def inverse(self) -> list:
        """
        Renvoie l'inverse de la Matrice.
        """
        if not self.is_squared():
            return None
        if self.det == 0:
            return None
        M = self.comatrice().transposee()*(1/self.det)
        return M

    def trace(self) -> float:
        """
        Renvoie la trace de la Matrice.
        """
        if not self.is_squared():
            return None
        M = self.value
        return sum([M[i][j] for i in range(len(M)) for j in range(len(M[i])) if i == j])


def phi(p: int, i: int) -> int:
    if p < i:
        return p
    return p+1


def random_matrix(n: int) -> Matrice:
    rg = range(n)
    return Matrice([[randint(-9, 9) for _ in rg] for _ in rg])


def create_matrix(M: list) -> Matrice:
    return Matrice(M)
