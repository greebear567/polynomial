from polynomial import polynomial
from Lagrange_polynomial import lagrange

b = polynomial(1,1)
c = polynomial(1, -0)
print(b.mult(c).coeff)
a = lagrange({'-1' : 1, '0' : 0, '1' : 1})
print(a.coeff)
a.coeff=polynomial.enlarger_of_power(a.coeff, 4)
print(a.coeff)
