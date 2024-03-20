from  datetime import  date
atual = date.today().year
nascimento = int(input('digite o ano do seu nascimento : '))
idade = atual - nascimento
print('Quem nasceu no ano de {} tem {} anos de idade em {} '.format(nascimento, idade, atual))
if idade <= 9:
    print('você se encaixa perfeitamente na modalidade MIRIM !')
elif idade <= 14:
    print('você se encaixa perfeitamente na modalidade INFANTIL !')
elif idade <= 19:
    print('você se encaixa perfeitamente na modalidade JUNIOR ')
elif idade <= 25:
    print('você se encaixa perfeitamente na modalidade SÊNIOR')
elif idade >= 26:
    print('você se encaixa perfeitamente na modalidade MASTER')
