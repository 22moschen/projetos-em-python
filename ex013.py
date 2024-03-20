salario = float(input('digite o salário : '))
reajuste = salario + ( salario * 15 / 100 )
print('O  salario era de R$:{:.2f}, e agora com o aumento de 15% será R$:{:.2f} ' .format(salario, reajuste))