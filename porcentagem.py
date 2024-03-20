pro = int(input('digite o valor do PRODUTO : R$'))
des = int(input('digite o valor do DESCONTO % : '))
cal = pro - (pro * des / 100)
print('O PRODUTO que custava R$:{:.2f} agora com o DESCONTO de: {}% passa a CUSTAR apenas: R${:.2f} '.format(pro, des, cal))