#IMC = m/a2
peso = float(input('Digite a peso em kg: '))
altura = float(input('Digite a altura em m : '))
IMC = peso / (altura ** 2)
print('O peso é {} e a altura é {:.2f} e seu IMC é igual à {:.2f} !' .format(peso, altura, IMC))
if IMC <= 18:
    print('Abaixo do peso !')
elif IMC <= 25:
    print('Peso ideal !')
elif IMC <= 30:
    print('sobre peso !')
elif IMC <= 40:
    print('obesidade !')
else:
    print('Obesidade Mórbita !!! ;-;')