from polynomial import polynomial
import numpy as np

class lagrange(polynomial):
    def __init__(self, dict):
        self.coeff = lagrange.plnm_count(dict)

    @staticmethod
    def fundamental_plnm_count(curr_x : float, *a):
        # создаю в массиве множители знаменателя и потом перемножаю их в переменной знаменателя
        denominator = np.prod([curr_x-x for x in a if curr_x != x])

        arr = [polynomial(1, x) for x in a if x !=curr_x]
        res_plnm = polynomial()
        for every in arr:
            res_plnm = res_plnm.add(every)
        res_plnm = res_plnm.div(denominator)
        return polynomial()

    @staticmethod
    def plnm_count(dict):
        arr_plnm=[]
        for every in dict:
            arr_plnm.append(float(every)*lagrange.fundamental_plnm_count(dict[every], list(dict.values)))
        res_plnm = polynomial()
        for every in arr_plnm:
            res_plnm = res_plnm.add(every)
        return res_plnm
