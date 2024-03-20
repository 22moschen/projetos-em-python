nome = input('qual seu nome ')
sexo = input('informe seu genero [M/F] ').upper()
while sexo != 'F' and sexo != 'M':
    print('opção inválida, tente novamente ')
    sexo = input('informe seu Gênero ´[M/F]').upper()
if sexo == 'M':
    print('olá Senhor {}'.format(nome))
else:
    print('olá senhora {} '.format(nome))
