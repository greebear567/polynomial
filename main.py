from polynomial import polynomial

a= polynomial(1,2,3)
b= polynomial(1,3,2)
a.sub(b)
if type(a)==polynomial:
    print(1)
print(a.coeff)
print(type(a))