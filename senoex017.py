from math import radians, sin, cos, tan
ângulo = float(input('Digite o angulo que você deseja : '))
seno = sin(radians(ângulo))
print('O ângulo de : {:.0f} tem o SENO de : {:.2f} ' .format(ângulo, seno))
coseno = cos(radians(ângulo))
print('o ângulo de: {} tem o COSSENO de: {:.2f} ' .format(ângulo, coseno))
tangente = tan(radians(ângulo))
print('o ângulo de: {} tem a TANGENTE de: {:.2f} ' .format(ângulo, tangente))