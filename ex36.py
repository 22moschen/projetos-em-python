i = float(input('digite o valor do imóvel R$: '))
s = int(input('digite o valor do seu salário R$: '))
a = int(input('digite a quantidade de anos em que você deseja ultilizar pra efetuar o pagamento total : '))
b = a * 12
cal = i / b
m = s * 30 / 100
print(' Para pagar uma casa de {:.2f} em {} anos o valor da parcela será de R$:{:.2f}'.format(i, a, cal))
if cal <= m:
    print('O emprestimo PODE ser CONCEDIDO :)')
else:
    print('Emprestimo NEGADO ;-; ')

#print('COMPARANDO pra pagar o valor é {} e o minimo é {} '.format(cal, m))
#cuidado pra não esquecer o nome das variavel kkkkk