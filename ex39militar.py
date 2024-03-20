from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
if idade == 18:
    print('Você tem que se alistar imediatamente !')
elif idade < 18:
    saldo = 18 - idade
    print('ainda faltam {} anos pra vc se alistar !'.format(saldo))
    ano = atual + saldo
    print('seu alistamento será no ano de {} ;-; !'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado á {} anos !'.format(saldo))
    ano = atual - saldo
    print('seu alistamento foi no ano de {} :( !'.format(ano))
