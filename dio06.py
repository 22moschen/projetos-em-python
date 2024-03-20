conjunto = {1, 2, 3, 4, 5}
conjunto2 = {5, 6, 7, 8}
comjunto_uniao = conjunto.union(conjunto2)
print('União : {} '.format(comjunto_uniao))
conjunto_interseccao = conjunto.intersection(conjunto2)
print('intersecção : {} '.format(conjunto_interseccao))
conjunto_diferenca1 = conjunto.difference(conjunto2)
conjunto_diferenca2 = conjunto2.difference(conjunto)
print('Diferença entre 1 e 2 : {} '.format(conjunto_diferenca1))
print('Diferença entre 2 e 1 {} '.format(conjunto_diferenca2))
conjunto_diff_semetrica = conjunto.symmetric_difference(conjunto2)
print('diferença simétrica: {} '.format(conjunto_diff_semetrica))

conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5}
conjunto_sbset = conjunto_a.issubset(conjunto_b)
print('B é um subconjunto ge A ? {} '.format(conjunto_sbset))
conjunto_superset = conjunto_b.issuperset(conjunto_a)
print('A é um subconjunto de B ? {} '.format(conjunto_superset))
#conjunto = {1, 2, 3, 4}
#conjunto.add(5)
#conjunto.discard(2)
#print(conjunto)