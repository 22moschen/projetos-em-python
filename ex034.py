a = int(input('digite o valor do seu salário R$: '))
if a <= 1250:
    novo = a + (a * 15 / 100)
else:
    novo = a + (a * 10 / 100)
print('Quem ganhava R${:.2f} agora passa a ganhar R${:.2f} '.format(a,novo))