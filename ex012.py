preco = float(input('qual o valor original do produto ? '))
desconto = preco - (preco * 5 / 100)
print('O produto custa R$:{:.2f}, mas como a loja está com promoção de 5% ele passará a custar R$:{:.2f} ' .format(preco, desconto))