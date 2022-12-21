import numpy as np


class polynomial:
    """класс для работы с полиномами"""
    def __init__(self, *a):
        self.coeff = np.array(a)
        self.power = len(self.coeff) - 1

    def enlarger_of_power(self: np.ndarray, big_power):
        """увеличение степенин полинома"""

        while len(self) < big_power:
            self = np.append(self, 0)
        return self

    def add(self, second_plnm):
        """сложение"""

        if len(self.coeff) > len(second_plnm.coeff):
            second_plnm.coeff = polynomial.enlarger_of_power(second_plnm.coeff, len(self.coeff))
            self.coeff += second_plnm.coeff
            return self
        if len(self.coeff) < len(second_plnm.coeff):
            self.coeff = polynomial.enlarger_of_power(self.coeff, len(second_plnm.coeff))
            self.coeff += second_plnm.coeff
            return self
        self.coeff += second_plnm.coeff
        return self

    def sub(self, second_plnm):
        """вычитание"""

        if len(self.coeff) > len(second_plnm.coeff):
            second_plnm.coeff = polynomial.enlarger_of_power(second_plnm.coeff, len(self.coeff))
            self.coeff -= second_plnm.coeff
            return self
        if len(self.coeff) < len(second_plnm.coeff):
            self.coeff = polynomial.enlarger_of_power(self.coeff, len(second_plnm.coeff))
            self.coeff -= second_plnm.coeff
            return self
        self.coeff -= second_plnm.coeff
        return self

    def mult(self, some):
        """умножение"""

        if type(some) == polynomial:
            res_plnm=polynomial()
            res_plnm.coeff = polynomial.enlarger_of_power(res_plnm.coeff, len(self.coeff)+len(some.coeff)-1)
            for i in range(len(self.coeff)):
                for j in range(len(some.coeff)):
                    res_plnm.coeff[i+j] += self.coeff[i]*some.coeff[j]
            return res_plnm
        else:
            self.coeff *= some
            return self

    def div(self, some):
        """деление на число"""

        self.coeff /= some
        return self
