num = int(input('digite um numero: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end= '')
        tot += 1
    else:
        print('\033[31m', end= '')
    print('{} '.format(c), end= '')
print(' \n\033[m o numero {} foi dividido {} vezes'.format(num, tot))
if tot == 2:
    print('por isso ele é PRIMO !!')
else:
    print('E por isso ele NÃO É PRIMO !!!')