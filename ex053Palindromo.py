frase = str(input('Digite uma frase :')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
#método utilizando o (for)
#inverso = ''
#for letra in range(len(junto) - 1, -1, -1):
#    inverso += junto[letra]
print('o inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um PALINDROMO !')
else:
    print(' A frase digitada NÃO É UM PALINDROMO !')