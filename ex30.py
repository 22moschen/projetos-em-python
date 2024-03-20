número = int(input('digite um numero qualquer : '))
resultado = número % 2
if resultado ==  0:
    print('O número é {} par '.format(número))
else:
    print('O numero é {} impar'.format(número))