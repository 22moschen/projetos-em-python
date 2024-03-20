largura = float(input('largura da parede : '))
altura = float(input('altura da parede : '))
área = largura * altura
print('sua parede tem a dimensão de {}x{} e sua área é {}' .format(largura, altura, área))
tinta = área / 2
print('para pintar está parede será nescessário {} litros de tinta ! ' .format(tinta))