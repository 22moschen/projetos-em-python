soma = 0
cont = 0
par = 0
for c in range (1, 7):
    num = float(input('digite o {}° numero : '.format(c)))
    if num % 2 == 0:
        soma += num
        par += 1
    cont += 1
print('você informou {} numeros \n Mas apenas {} são PARES \n Sendo a soma entre eles igual á {:.0f} '.format(cont, par, soma))