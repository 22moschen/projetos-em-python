km = float(input('quantos km foram percorridos ? '))
v = km * 0.15
print('vc percorreu {:.0f}km com o automovel, e deverá pagar R$:{:.2f} ' .format(km, v))
d = float(input('qual a quantidade de dias o automovel ficou sob sua responsabilidade ? '))
a = d * 60 + v
print('vc ficou {}dias com o carro e deverá pagar R$:{:.2f} ' .format(d, a))