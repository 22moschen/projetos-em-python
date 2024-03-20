distancia = float(input('qual a distancia ? '))
print('vc está prestes acomecar uma viagem de {} km'.format(distancia))
preço = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('O preço da sua viagem é de R$:{:.2f} '.format(preço))