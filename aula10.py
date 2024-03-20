n1 = float(input('digite a primeira nota :'))
n2 = float(input('digite a segunda nota :'))
m = (n1 + n2)/2
print('a sua média foi {:.0f}'.format(m))
print('PARABÉS' if m >=6 else 'ESTUDE MAIS!')