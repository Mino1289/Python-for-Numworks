from __future__ import annotations
from random import randint
from typing import Union
from math import atan


class Matrice:
    """
    Représente une Matrice dans Python, avec une représentation en rectangle.
    """

    def __init__(self, M: list[list[float]]) -> None:
        self.value = M

    def __repr__(self):
        return str(self)

    def __len__(self) -> int:
        return len(self.value)

    def __getitem__(self, i)->list[float]:
        return self.value[i]

    def __iter__(self):
        return iter(self.value)

    def __eq__(self, M: Union[list[list[float]], Matrice]) -> bool:
        if len(self.value) == len(M) and len(self.value[0]) == len(M[0]):
            for i in range(len(M)):
                for j in range(len(M[i])):
                    if self.value[i][j] != M[i][j]:
                        return False
            return True
        return False

    def __ne__(self, M: Union[list[list[float]], Matrice]) -> bool:
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

    def __add__(self, M: Matrice) -> Matrice:
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

    def __sub__(self, M: Matrice) -> Matrice:
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

    def __mul__(self, M: Union[Matrice, Vecteur, float, int, complex]) -> Matrice:
        if isinstance(M, Matrice) or isinstance(M, Vecteur):
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

    def __pow__(self, n: int) -> Matrice:
        if not self.is_squared():
            return Matrice([[0]])
        if n == 0:
            return self.identity(len(self))
        if n == 1:
            return self
        if n < 0:
            MI = self.inverse()
            M = MI
            for _ in range(abs(n+1)):
                M *= MI
            return M
        M = self
        for _ in range(n-1):
            M *= self
        return M

    def __neg__(self) -> Matrice:
        return self*(-1)

    def __pos__(self) -> Matrice:
        return self

    def __abs__(self) -> Matrice:
        x, y = len(self.value), len(self.value[0])
        for i in range(x):
            for j in range(y):
                self.value[i][j] = abs(self.value[i][j])
        return self

    def __round__(self, n: int = 0) -> Matrice:
        x, y = len(self.value), len(self.value[0])
        for i in range(x):
            for j in range(y):
                self.value[i][j] = round(self.value[i][j], n)
        return self

    def identity(self, n: int) -> Matrice:
        """
        Renvoie la matrice identité d'ordre n.
        """
        M = []
        for i in range(n):
            L = []
            for j in range(n):
                L.append(1) if i == j else L.append(0)
            M.append(L)
        return Matrice(M)

    def is_squared(self) -> bool:
        """
        Renvoie un booléen, si la matrice est carrée.
        """
        if len(self) != 0:
            return len(self.value) == len(self.value[0])
        return False

    def determinant(self) -> float:
        """
        Renvoie le déterminant de la matrice.
        """
        n = len(self)
        if n == 0:
            return 1
        s = 0
        for j in range(n):
            s += self[0][j] * self.cofacteur(0, j)
        return s

    def cofacteur(self, i: int, j: int) -> int:
        """
        Renvoie le cofacteur de la matrice en i, j.
        """
        m = self.mineur(i, j)
        if (i + j) % 2 == 0:
            return m
        return -m

    def supprimer_ligne_colone(self, i: int, j: int) -> Matrice:
        """
        Renvoie la matrice de taille n-1 ou la ligne i et la colonne j ont été supprimé.
        """
        n = len(self)
        rg = range(n-1)
        B = [[None for _ in rg] for _ in rg]
        for p in rg:
            for q in rg:
                B[p][q] = self[phi(p, i)][phi(q, j)]
        return Matrice(B)

    def mineur(self, i: int, j: int) -> int:
        """
        Renvoie le mineur de la matrice en i j.
        """
        A1 = self.supprimer_ligne_colone(i, j)
        return A1.determinant()

    def comatrice(self) -> Matrice:
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

    def transposee(self) -> Matrice:
        """
        Renvoie la transposée de la matrice.
        """
        m, n = len(self.value), len(self.value[0])
        B = [[None for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                B[i][j] = self.value[j][i]
        return Matrice(B)

    def inverse(self) -> Matrice:
        """
        Renvoie l'inverse de la matrice.
        """
        if not self.is_squared():
            return None
        if self.determinant() == 0:
            return None
        M = self.comatrice().transposee()*(1/self.determinant())
        return Matrice(M)

    def trace(self) -> float:
        """
        Renvoie la trace de la matrice.
        """
        if not self.is_squared():
            return None
        M = self.value
        return sum([M[i][j] for i in range(len(M)) for j in range(len(M[i])) if i == j])


class Vecteur:
    """
    Représente un vecteur dans Python avec une représentation en colonne.
    """

    def __init__(self, M: list) -> None:
        if len(M) >= 2 and len(M[0]) == 1:
            self.value = M
        else:
            raise ValueError("Ce n'est pas un vecteur")

    def __repr__(self):
        return str(self)

    def __len__(self) -> int:
        return len(self.value)

    def __getitem__(self, i):
        return self.value[i]

    def __iter__(self):
        return iter(self.value)

    def __eq__(self, M: Union[list, Vecteur]) -> bool:
        if len(self.value) == len(M) and len(self.value[0]) == len(M[0]):
            for i in range(len(M)):
                for j in range(len(M[i])):
                    if self.value[i][j] != M[i][j]:
                        return False
            return True
        return False

    def __ne__(self, M: Union[list, Vecteur]) -> bool:
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

    def __add__(self, M: Vecteur) -> Vecteur:
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

    def __sub__(self, M: Vecteur) -> Vecteur:
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

    def __mul__(self, M: Union[Vecteur, Point, float, int, complex]) -> Union[Matrice, Vecteur, int, float]:
        if isinstance(M, Point):
            m = []
            if len(M) != 1:
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
        if isinstance(M, Vecteur):
            m = 0
            if len(self.value) != len(M):
                return m
            for i in range(len(self.value)):
                m += self[i][0] * M[i][0]
            return m
        if isinstance(M, float) or isinstance(M, int) or isinstance(M, complex):
            n, m = len(self), len(self[0])
            B = [[None for _ in range(m)] for _ in range(n)]
            for i in range(n):
                for j in range(m):
                    B[i][j] = self[i][j] * M
            return Vecteur(B)
        return self

    def __neg__(self) -> Vecteur:
        return self*(-1)

    def __pos__(self) -> Vecteur:
        return self

    def __abs__(self) -> Vecteur:
        x, y = len(self.value), len(self.value[0])
        for i in range(x):
            for j in range(y):
                self.value[i][j] = abs(self.value[i][j])
        return self

    def __round__(self, n: int = 0) -> Vecteur:
        x, y = len(self.value), len(self.value[0])
        for i in range(x):
            for j in range(y):
                self.value[i][j] = round(self.value[i][j], n)
        return self

    def norme(self) -> Union[int, float]:
        """
        Renvoie la norme du vecteur.
        """
        m = 0
        for k in range(len(self)):
            m += self[k][0]**2
        return round(m**0.5, 2)

    def angle(self) -> Union[int, float]:
        """
        Renvoie l'angle entre le vecteur et l'axe des abscisses.
        """
        if len(self) != 2:
            return None
        x, y = self[0][0], self[1][0]
        t = atan(y/x)
        return round(t, 2)

    def plot(self, x: float = 0, y: float = 0, c: str = "black") -> None:
        """
        Ajoute au graphique en cours, le vecteur, sous forme d'une fleche à partir de l'origine, ou à partir de x,y données en argument, couleur facultative (noir d'origine)
        """
        import matplotlib.pyplot as plt
        if len(self) != 2:
            return None
        dx, dy = self[0][0], self[1][0]
        plt.arrow(x, y, dx, dy, head_width=self.norme()/50, fc=c, ec=c)

    def transformation(self, P: Point) -> Point:
        """
        Renvoie le Point issue du déplacement du Point donné en arguments par le vecteur. 
        """
        if len(P) != len(self[0]):
            return P
        for i in range(len(self)):
            P[0][i] += self[i][0]
        return P


class Point:
    """
    Représente un point dans Python, avec une représentation en ligne.
    """

    def __init__(self, M: Union[list, tuple]) -> None:
        P = []
        if isinstance(M, tuple) and len(M) >= 1:
            P.append(list(M))
            self.value = P
            return
        # liste de liste, ici on a une seule liste, contenant 1 seule liste
        if isinstance(M, list) and len(M) == 1:
            self.value = M

    def __repr__(self):
        return str(self)

    def __len__(self) -> int:
        return len(self.value)

    def __getitem__(self, i: int):
        return self.value[i]

    def __iter__(self):
        return iter(self.value)

    def __eq__(self, M: Union[list, Point]) -> bool:
        if len(self.value) == len(M) and len(self.value[0]) == len(M[0]):
            for i in range(len(M)):
                for j in range(len(M[i])):
                    if self.value[i][j] != M[i][j]:
                        return False
            return True
        return False

    def __ne__(self, M: Union[list, Point]) -> bool:
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
        tp = str(tuple(self.value[0])) + "\n"
        return tp

    def __mul__(self, M: Union[Matrice, float, int, complex]) -> Point:
        if isinstance(M, Matrice):  # P * M => P
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
            return Point(m)
        if isinstance(M, float) or isinstance(M, int) or isinstance(M, complex):
            n, m = len(self), len(self[0])
            B = [[None for _ in range(m)] for _ in range(n)]
            for i in range(n):
                for j in range(m):
                    B[i][j] = self[i][j] * M
            return Point(B)
        return self

    def __neg__(self) -> Point:
        return self*(-1)

    def __pos__(self) -> Point:
        return self

    def __abs__(self) -> Point:
        x, y = len(self.value), len(self.value[0])
        for i in range(x):
            for j in range(y):
                self.value[i][j] = abs(self.value[i][j])
        return self

    def __round__(self, n: int = 1) -> Point:
        x, y = len(self.value), len(self.value[0])
        for i in range(x):
            for j in range(y):
                self.value[i][j] = round(self.value[i][j], n)
        return self

    def dist(self, P: Point) -> Union[int, float]:
        """
        Renvoie la distance entre le Point, et celui donnée en arguments.
        """
        if len(self[0]) != len(P[0]):
            return
        m = 0
        for k in range(len(self[0])):
            m += (self[0][k]-P[0][k])**2
        return m**0.5

    def plot(self, c: str = "red") -> None:
        """
        Ajoute au graphique en cours le point, couleur facultative (rouge d'origine)
        """
        from matplotlib import pyplot as plt
        if len(self[0]) != 2:
            return None
        x, y = self[0][0], self[0][1]
        plt.scatter(x, y, color=c)


def phi(p: int, i: int) -> int:
    if p < i:
        return p
    return p+1


def random_matrix(n: int) -> Matrice:
    rg = range(n)
    return Matrice([[randint(-9, 9) for _ in rg] for _ in rg])


def newmatrice(M: list) -> Matrice:
    return Matrice(M)
