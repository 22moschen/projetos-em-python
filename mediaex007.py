n1 = float(input('digite a primeira nota do aluno : '))
n2 = float(input('digite a segunda nota do aluno : '))
média = (n1 + n2) / 2
print('A primeira nota foi : {}, e a segunda nota foi : {},' .format(n1, n2))
print('A Média foi {} ' .format(média,))
if 7 > média >= 5:
    print('o aluno está em RECUPERAÇÃO !')
elif média <= 5:
    print('o aluno está REPROVADO ! :(')
else: média >= 5.5
print('o aluno está APROVADO !!! :) ')
