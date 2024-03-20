vel = float(input('informe a velocidade do veiculo :'))
if vel > 80:
    print('vc ultrapassou a velocidade')
    multa = (vel - 80) * 7
    print('você foi altuado em deverá pagar uma muta no valor de R$:{}'.format(multa))
print('tenha um bom dia. dirija com segurança ')