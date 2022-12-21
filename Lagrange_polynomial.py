from polynomial import polynomial
import numpy as np

class lagrange(polynomial):
    """класс для подсчета полиномов лагранжа"""

    def __init__(self, dict):
        self.coeff = lagrange.plnm_count(**dict)

    @staticmethod
    def fundamental_plnm_count(curr_x : float, *a):
        """считает фундаментальные полиномы"""

        # создаю в массиве множители знаменателя и потом перемножаю их в переменной знаменателя
        a=a[0]#извлек из кортежа нужный массив иксов функции
        denominator = np.prod([(curr_x-x) for x in a if curr_x != x])
        print("знаменатель фундаментального полинома равен =", denominator)


        arr = [polynomial(1, -x) for x in a if x != curr_x]
        #print([x.coeff for x in arr])
        res_plnm = polynomial()
        k=0#переменная чтобы понять в первый раз заходим в цикл или нет
        for every in arr:
            if k != 0:
                res_plnm = res_plnm.mult(every)
            else:
                k=1
                res_plnm.coeff = every.coeff

        res_plnm = res_plnm.div(denominator)
        print(res_plnm.coeff)
        return res_plnm


    @staticmethod
    def plnm_count(**kwargs):
        """считает полином лагранжа"""

        arr_plnm=[]
        for every in kwargs.keys(): #в ключах мы храним иксы, в значениях храним значения функции
            arr_plnm.append(lagrange.fundamental_plnm_count(float(every), [float(x) for x in kwargs.keys()]).mult(float(kwargs[every])))
        res_plnm = polynomial()
        for every in arr_plnm:
            res_plnm = res_plnm.add(every)
        return res_plnm.coeff
