import random

opcoes = ["1", "2", "3", "4", "5"]

while True:
    print("Escolha sua jogada: ['1', '2', '3', '4', '5']")
    jogada = input().lower()

    while jogada not in opcoes:
        print("Jogada inválida. Escolha novamente.")
        jogada = input().lower()

    jogada_computador = random.choice(opcoes)
    print("O computador escolheu:", jogada_computador)

    if jogada == jogada_computador:
        print("Empate!")
    elif jogada == "pedra":
        if jogada_computador == "papel":
            print("Você perdeu!")
        else:
            print("Você ganhou!")
    elif jogada == "papel":
        if jogada_computador == "tesoura":
            print("Você perdeu!")
        else:
            print("Você ganhou!")
    elif jogada == "tesoura":
        if jogada_computador == "pedra":
            print("Você perdeu!")
        else:
            print("Você ganhou!")

    jogar_novamente = input("Quer jogar novamente? (s/n)").lower()
    if jogar_novamente != "s":
        break
