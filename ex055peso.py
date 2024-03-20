maior = 0
menor = 0
for p in range(1, 6):
        peso = float(input('digite o peso kg da {}° pessoa '.format(p)))
        if p == 1:
            maior = p
            menor = p
        else:
            if peso > maior:
               maior = peso
            elif peso <= menor:
                menor = peso
print(' o maior peso lido foi o de {:.2f}kg'.format(maior))
print('o menor peso a ser digitado foi {:.2f}kg'.format(menor))
