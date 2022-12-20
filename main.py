from polynomial import polynomial

a = polynomial(1, 2)
b = polynomial(1, 3, 2)
a.add(b)
print(a.coeff)
print(type(a))
