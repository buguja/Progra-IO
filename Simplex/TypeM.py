__author__ = 'José Pablo'

from fractions import Fraction


class M:
    def __init__(self, r, m=0):
        self.r = r
        self.m = m

    def __add__(self, other):
        if isinstance(other, int) or isinstance(other, float) or isinstance(other, complex):
            return M(self.r + other, self.m)
        if isinstance(other, Fraction):
            return M(self.r + other, self.m)
        if isinstance(other, M):
            return M(self.r + other.r, self.m + other.m)

    def __sub__(self, other):
        if isinstance(other, int) or isinstance(other, float) or isinstance(other, complex):
            return M(self.r - other, self.m)
        if isinstance(other, Fraction):
            return M(self.r - other, self.m)
        if isinstance(other, M):
            return M(self.r - other.r, self.m - other.m)

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float) or isinstance(other, complex):
            return M(self.r * other, self.m * other)
        if isinstance(other, Fraction):
            return M(self.r * other, self.m * other)
        if isinstance(other, M):
            if other.m == 0:
                return M(self.r * other.r, self.m * other.r)
            if self.m == 0:
                return M(other.r*self.r,other.m*self.r)
            raise NotImplemented

    def __truediv__(self, other):
        if isinstance(other, int) or isinstance(other, float) or isinstance(other, complex):
            return M(self.r / other, self.m)
        if isinstance(other, Fraction):
            return M(self.r / other, self.m)
        if isinstance(other, M):
            if other.m == 0:
                return M(self.r / other.r, self.m / other.r)
            raise NotImplemented

    def __lt__(self, other):
        if isinstance(other, int) or isinstance(other, float) or isinstance(other, complex) or isinstance(other,
                                                                                                          Fraction):
            if self.m == 0:
                return self.r < other
            else:
                return self.m < 0
        if isinstance(other, M):
            if self.m == other.m:
                return self.r < other.r
            else:
                return self.m < other.m

    def __le__(self, other):
        if isinstance(other, int) or isinstance(other, float) or isinstance(other, complex) or isinstance(other,
                                                                                                          Fraction):
            if self.m == 0:
                return self.r <= other
            else:
                return self.m <= 0
        if isinstance(other, M):
            if self.m == other.m:
                return self.r <= other.r
            else:
                return self.m <= other.m

    def __gt__(self, other):
        if isinstance(other, int) or isinstance(other, float) or isinstance(other, complex) or isinstance(other,
                                                                                                          Fraction):
            if self.m == 0:
                return self.r > other
            else:
                return self.m > 0
        if isinstance(other, M):
            if self.m == other.m:
                return self.r > other.r
            else:
                return self.m > other.m

    def __ge__(self, other):
        if isinstance(other, int) or isinstance(other, float) or isinstance(other, complex) or isinstance(other,
                                                                                                          Fraction):
            if self.m == 0:
                return self.r >= other
            else:
                return self.m >= 0
        if isinstance(other, M):
            if self.m == other.m:
                return self.r >= other.r
            else:
                return self.m >= other.m

    def __eq__(self, other):
        if isinstance(other, int) or isinstance(other, float) or isinstance(other, complex) or isinstance(other,
                                                                                                          Fraction):
            if self.m == 0:
                return self.r == other
            else:
                return False
        if isinstance(other, M):
            return self.r == other.r and self.m == other.m

    def __ne__(self, other):
        if isinstance(other, int) or isinstance(other, float) or isinstance(other, complex) or isinstance(other,
                                                                                                          Fraction):
            if self.m == 0:
                return self.r != other
            else:
                return True
        if isinstance(other, M):
            return self.r != other.r or self.m != other.m

    def __radd__(self, other):
        return self+other

    def __str__(self):
        if self.r == 0:
            return "{}{}".format(self.m,"M" if self.m!=0 else "")
        elif self.m == 0:
            return "{}".format(self.r)
        else:
            return "{}{} {}M".format(self.r," +" if self.m >0 else "" ,self.m)
