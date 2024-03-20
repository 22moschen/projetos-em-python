Primeiro = int(input('digite o primeiro termo :'))
Razão = int(input('digite A RAZÃO :'))
num = 1
termo = Primeiro
while num <= 10:
  print('{} > '.format(termo), end=  '')
  num += 1
  termo += Razão

