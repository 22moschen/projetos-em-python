from  random import randint
computador = randint(0, 10)
print('vamos começar um jogo, e ele funcionará mais ou menos assim; \n eu vou pensar em um número de [1 á 10] \n e VC TENTARÁ  adivinhar ... ')
acertou = False
chances = 0
while not acertou:
    jogador = int(input('Digíte um número de [1 à 10] : '))
    chances += 1
    if jogador != 1 and jogador != 2 and jogador != 3 and jogador != 4 and jogador != 5 and jogador != 6 and jogador != 7 and jogador != 8 and jogador != 9 and jogador != 10:
        print('opção inválida, Tente Novamente')
    elif jogador == computador:
        acertou = True
    elif jogador < computador:
        print('>MAIS<')
    elif jogador > computador:
        print('>MENOS<')
print('PARABÉNS VOCÊ GANHOU !')
print('MAS FORAM NESCESSÁRIAS {} tentativas '.format(chances))