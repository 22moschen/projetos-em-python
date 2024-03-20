from random import randint
itens = ('PEDRA', 'PAPEL', 'TESOURA' )
computador = randint(0, 2)
print('''suas opções:
[ 0 ] PEDRA 
[ 1 ] PAPEL 
[ 2 ] TESOURA ''')
jogador = int(input('Qual é a sua jogada ? '))
print('-=' * 11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 11)
if computador == 0: # se o computador jogou PEDRA
    if jogador == 0:
        print('EMPATE !')
    elif jogador == 1:
        print('JOGADOR VENCE !')
    elif jogador == 2:
        print('COMPUTADOR VENCE !')
    else:
        print('Jogada invàlida !')
elif computador == 1: # se o computador jogou PAPEL
    if jogador == 1:
        print('EMPATE !!')
    elif jogador == 2:
        print('COMPUTADOR VENCE !')
    elif jogador == 0:
        print('JOGADOR VENCE !')
    else:
        print('Jogada invàlida !')
elif computador == 2: # se o computador jogou TESOURA
    if jogador == 2:
        print('EMPATE !')
    elif jogador == 1:
        print('COMPUTADOR VENCE !')
    elif jogador == 0:
        print('JOGADOR VENCE !')
    else:
        print('Jogada invàlida !')