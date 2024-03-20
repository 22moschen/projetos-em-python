print('-=' * 50)
print(            '*$*$*$*$  '    'LOJAS MOSCHEN'     '  $*$*$*$*'            )
print('-=' * 50)
valor = float(input('informe o valor da compra R$ : '))
print('FORMAS DE PAGAMENTO')
resposta = float(input('Qual será a forma de pagamento ? \n [ 1 ] à vista dinheiro/cheque: \n [ 2 ] á vista no cartão: \n [ 3 ] Em até 2x no cartão \n [ 4 ] 3x ou mais no cartão \n\n RESPOSTA :  '))
if resposta != 1 and resposta != 2 and resposta != 3 and resposta != 4:
    print('Por favor Digite uma opção VALIDA !!')
#se o usuario escolher a opção 1 será descontado 10%
elif resposta == 1:
    calculo = valor - (valor * 10 / 100)
    print('como sua compra será paga de de forma á vista terá um desconto de 10% ! :) \n E passará a custar R$:{:.2f}'.format(calculo))
    print(' AGRADECEMOS A PREFERÊNCIA !! ')
#se o usuario escolher a opção 2 será descontado 5%
elif resposta == 2:
    calculo = valor - (valor * 5 / 100)
    print('como sua compra será paga á vista no cartão,terá um desconto de 5% !  \n E passará a custar R$:{:.2f} . '.format(calculo))
    print(' AGRADECEMOS A PREFERÊNCIA !! ')
#se o usuario  escolher a opção 3 será cobrado o valor original
elif resposta == 3:
    print('sua compra será no valor de R$:{:.2f} '.format(valor))
    print(' AGRADECEMOS A PREFERÊNCIA !! ')
#se o usuario escolher a opção 4 será cobrado 20% de juros
elif resposta == 4:
    calculo = valor + (valor * 20 / 100)
    print('como sua compra foi parcelada em mais de 3x no cartão, será cobrado 20% de juros \n E o valor será de R$:{} !'.format(calculo))
    print(' AGRADECEMOS A PREFERÊNCIA !! ')
#– à vista dinheiro/cheque: 10% de desconto

#– à vista no cartão: 5% de desconto

#– em até 2x no cartão: preço formal

#– 3x ou mais no cartão: 20% de juros