n1 = int(input('Digite o primeiro Numero :'))
n2 = int(input('Digite o segundo Numero :'))
if n1 > n2:
    print('O Numero {} é maior que o Numero {} !'.format(n1, n2))
elif n1 < n2:
    print('O Numero {} é menor que o Numero {} !'.format(n1, n2))
elif n1 == n2:
    print('O Numero {} é exatamente igual ao Numero {} !'.format(n1, n2))