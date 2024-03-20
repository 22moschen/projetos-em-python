num = int(input('informe um número : '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('analisando número... ' .format(num))
print(' A Unidade é {}'.format(u))
print(' A Dezena é {}'.format(d))
print(' A Centena é {}'.format(c))
print(' E o Milhar é {} ;)'.format(m))