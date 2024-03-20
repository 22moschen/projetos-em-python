#Calculando área
resposta = int(input('Qual a forma do terreno á ser CALCULADA ?? \n1) QUADRADO \n2) RETÂNGULO \n3) TRIÂNGULO \n4) TRAPÉZIO \n\n  Resposta : '))
if (resposta != 1 and resposta != 2 and resposta != 3 and resposta != 4):
    print('Digite uma opção valida !!')
else:
   if (resposta == 1):
      lado = float(input('qual o valor do lado do quadrado ?'))
      area = lado*lado
      print('O Quadrado informado tem a área igual a {:.2f} m2 '.format(area))
      opção = float(input('deseja calcular a area do triangulo ? \n se SIM diite [ 1 ] :'))
      if opção == 1:
         perimetro = lado * 4
         print('O PERIMETRO DO QUADRADO INFORMADO É {}'.format(perimetro))


      #Retangulo
   if (resposta == 2):
      base = int(input('Digite o valor da base do RETÂNGULO em ( m ) : '))
      altura = int(input('Digite o valor da altura RETÂNGULO em ( m ) : '))
      area = base * altura
      perimetro = (base * 2) + (altura * 2)
      print('O valor da Base do RETÂNGULO é {} e a Altura é {} então a área é igual a {:.1f} m2 \n E o Perimetro é {}'.format(base, altura, area, perimetro))
      #triangulo
   if (resposta == 3):
      base = float(input('Digite o valor da base do TRIÂNGULO em ( m ) : '))
      altura = float(input('Digite o valor da altura TRIÂNGULO em ( m ) : '))
      area = (base * altura) / 2
      print('a base do TRIÂNGULO é {} e a sua ALTURA é {} E A ÁREA É IGUAL A {} m2'.format(base, altura, area))
      opção = float(input('deseja calcular o perimetro do triangulo ? \n se SIM digite [ 1 ] :'))
      if opção == 1:
         lado1 = int(input('Digite o primeiro lado do triangulo :'))
         lado2 = int(input('Digite o segundo lado do triangulo :'))
         Perimetro = base + lado1 + lado2
         print('o PERIMETRO é {}'.format(Perimetro))

      #trapézio
   if (resposta == 4):
      base = float(input('Digite o valor da BASE MENOR do TRAPÉZIO em ( m ) : '))
      baseM = float(input('Digite o valor da BASE MAIOR TRAPÉZIO em ( m ) : '))
      altura = float(input('Digite o valor da altura TRAPÉZIO em ( m ) : '))
      area = (base + baseM) * altura / 2
      print('a área total do TRAPÉZIO é {} '.format(area))