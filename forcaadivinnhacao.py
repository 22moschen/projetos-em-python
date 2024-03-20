import forca
import adivinhacao

def escolhe_jogo():
    print("*********************************")
    print("*******Escolha o seu jogo!*******")
    print("*********************************")

    print("(1) Forca (2) Adivinhação")

    jogo = int(input("Qual jogo? "))

    if(jogo == 1):
        print("Jogando forca")
        forca.jogar()
    elif(jogo == 2):
        print("Jogando adivinhação")
        adivinhacao.jogar()

if(__name__ == "__main__"):
    escolhe_jogo()
# forca.py

enforcou = False
acertou = False

palavra_secreta = "python"
letras_acertadas = []
tentativas = 0

def chuta_letra(letra):
    global tentativas

    if(letra in palavra_secreta):
        letras_acertadas.append(letra)
        acertou = True
    else:
        tentativas += 1
        enforcou = True

def desenha_forca():
    print("  _______     ")
    print(" |/      |    ")

    if(enforcou and tentativas < 7):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(enforcou and tentativas == 7):
        print(" |      (_)   ")
        print(" |       |    ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print(" ")

def pega_letras_acertadas():
    return letras_acertadas

def jogo():
    desenha_forca()
    print("Letras acertadas: ", letras_acertadas)
    print("Tentativas: ", tentativas)

    letra = input("Qual letra? ")
    chuta_letra(letra)

    if(acertou):
        print("Você acertou!")
    elif(tentativas < 7 and not enforcou):
        print("Você errou!")
        desenha_forca()
    elif(tentativas == 7 and enforcou):
        print("Enforcado!")
    elif(acertou and enforcou):
        print("Você ganhou!")

jogo()

# adivinhacao.py

import random

def sorteia_numero():
    numero_secreto = random.randint(1, 10)
    return numero_secreto

def adivinha_numero():
    numero_secreto = sorteia_numero()
    tentativas = 0
    while(tentativas < 3):
        chute = int(input("Qual é o seu chute? "))
        tentativas += 1

        if(chute == numero_secreto):
            print("Você acertou!")
            break
        elif(chute < numero_secreto):
            print("Você errou! O número secreto é maior.")
        else:
            print("Você errou! O número secreto é menor.")

    if(chute != numero_secreto):
        print("Você perdeu!")

def jogar():
    adivinha_numero()

jogar()