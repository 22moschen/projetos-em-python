n1 = int(input('Digite o primeiro valor :'))
n2 = int(input('Digite o segundo valor : '))
opção = 0
while opção != 5:
    print('''
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos numeros
    [5] sair do programa ''')
    opção = int(input('qual é a sua opção ? :'))
    if opção == 1:
        cal = n1 + n2
        print('a soma entre dois numeros é {}'.format(cal))
    elif opção == 2:
        multiplicão = n1 * n2
        print('{} x {} = {}'.format(n1, n2, multiplicão))
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('o número {} é maior ! '.format(maior))
    elif opção == 4:
        print('Digite novos valores: ')
        n1 = int(input('informe um NOVO numero :'))
        n2 = int(input('informe um NOVO numero :'))
    elif opção == 5:
        print('finalizando...')
    else:
        print('opção invalida \n digite um numero entre [1 á 5] ')
print('Fim do Programa. Volte sempre ! :)')