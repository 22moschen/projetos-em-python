print('-='*20)
print('Analisador de Triângulos')
print('-='*20)
sg1 = float(input('Primeiro Seguimento :'))
sg2 = float(input('Segundo Seguimento :'))
sg3 = float(input('Terceiro Seguimento :'))
if sg1 < sg2 + sg3 and sg2 < sg1 + sg3 and sg3 < sg1 + sg2:
    print('Os segmentos acima PODEM formas TRIÂNGULOS :', end='')
    if sg1 == sg2 == sg3:
        print('equilatero!')
    elif sg1 != sg2 != sg3 != sg1:
        print('escaleno!')
    else:
        print('isóceles')
else:
    print('Os segmentos acima NÃO podem formar TRIÂNGULOS :')
