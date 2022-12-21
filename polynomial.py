import numpy as np


class polynomial:
    def __init__(self, *a):
        self.coeff = np.array(a)
        self.power = len(self.coeff) - 1

    def enlarger_of_power(self: np.ndarray, big_power):
        while len(self) < big_power:
            self = np.append(self, 0)
        return self

    def add(self, second_plnm):
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
        if type(some) == polynomial:
            if len(self.coeff) > len(some.coeff):
                some.coeff = polynomial.enlarger_of_power(some.coeff, len(self.coeff))
            if len(self.coeff) < len(some.coeff):
                self.coeff = polynomial.enlarger_of_power(self.coeff, len(some.coeff))
            self.coeff *= some.coeff
            return self
        else:
            self.coeff *= some.coeff
            return self

    def div(self, some):
        self.coeff /= some
        return self
