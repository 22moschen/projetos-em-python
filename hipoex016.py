from math import hypot
co = float(input('digite a dimensão do cateto oposto : '))
ca = float(input('digite a dimensão do cateto adjasente : '))
hi = hypot(co, ca)
print('A hipotenusa é igual a: {:.2f} ' .format(hi))
