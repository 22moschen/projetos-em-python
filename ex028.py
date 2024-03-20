import time
from random import  randint
totchances = 5
from time import sleep
computador = randint(0,5)#esse comando faz o computador pensar
print('-=-' * 20)
print('vou pensar em um numero entre 0 e 5. tente adivinhar :)')
print('-=-'* 20)
jogador = int(input('Em que numero eu pensei? :'))
while jogador != 1 and jogador != 2 and jogador != 3 and jogador != 4 and jogador != 5:
    print('tentativa invalida. digite um numero de [1 à 5]')
    jogador = int(input('Em que numero eu pensei? :'))
else:
    print('PROSSESANDO...')
time.sleep(2)#este comando faz com que o progama parar e espere por 2 segundo
if jogador == computador:
    print('PARABÉS VOCÊ VENCEU')
while jogador != computador:
    totchances -= 1
    print('Não eu não pensei nesse número !')
    print('vc tem mais {}°'.format(totchances))
    jogador = int(input('Em que numero eu pensei? :'))
    if jogador == computador:
        print('Parabéns você venceu :) ')
    elif totchances == 1:
        print('GAMER OVER !!! :(')
        print('eu pensei no numero {} '.format(computador))