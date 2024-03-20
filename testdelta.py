import math
print('equacao do segundo grau')
print('-------------------------')
v1 = int(input('informe o valor de A:'))
a = v1
v2 = int(input('informe o valor de B:'))
b = v2
v3 = int(input('informe o valor de C:'))
c = v3
print('--------------------------------')
print('sua equaçao e {}x2 + {}x + {} = 0 '.format(a, b, c))
delta = (b*b) - 4 * a * c
print('valor de delta = {}'.format(delta))
print('--------------------------------')
if delta < 0:
    print('para delta negativo nao existem raizes reais')
elif delta == 0:
     x1 = (-b + math.sqrt(delta)) / (2 * a)
     print('para delta igual a zero, temos duas raizes iguas à:{} '.format(x1))
else:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    print('para delta positivo,Raizes diferentes:')
    print('raiz x1:{}'.format(x1))
    print('raiz x2:{}'.format(x2))

print('````````````````````````')