real = float(input('Quanto de dinheiro vc tem na carteira ? '))
dolar = real / 5.53
print('com R$:{:.2f} vc consegue comprar U${} ' .format(real, dolar))