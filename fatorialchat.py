                         #codigo do python
#def fatorial(num):
#    if num == 0:
#        return 1
#    else:
#        return num * fatorial(num-1)

# exemplo de uso
#n = int(input('Digíte um numero inteiro :'))
#resultado = fatorial(n)
#print("O fatorial de", n, "é", resultado
                 #meu codigo  :)
#from math import factorial
#n = int(input("digite um numero inteiro :"))
#cal = n * factorial(n-1)
#print(" o resutado {}".format(cal))
             #codigo ultilizando o while
n = int(input("digite um numero inteiro :"))
c = n
f = 1
print('calculando {}! = '.format(n), end='')
while c > 0:
    print('{} ' .format(c), end='')
    print(' x 'if c > 1 else' = ', end='')
    f *= c
    c -= 1
print('{} é {}'.format(n,f))