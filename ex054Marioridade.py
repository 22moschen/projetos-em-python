from datetime import date
atual = date.today().year
totMaior = 0
totMenor = 0
for press in range(1, 8):
    nascimento = int(input('digite o ano em que a {}° pessoa nasceu :'.format(press)))
    cal = atual - nascimento
    if cal >= 21:
        totMaior += 1
    else:
        totMenor += 1
print('ao todo temos {} pessoas maiores de idade '.format(totMenor))
print('ao todo temos {} pessoas menores de idade '.format(totMaior))
