lista = [1, 2, 3, 4, 5, 6, 7]
lista_animal = ('cachorro', 'gato', 'elefante', 'arara' )
lista_animal = 'macaco'
print(lista_animal)
tupla = (1, 10, 12, 14)
print(len(tupla))
print(len(lista_animal))
tupla_animal = tuple(lista_animal)
print(type(tupla_animal))
lista_numerica = list(tupla)
print(type(lista_numerica))
lista_numerica[0] = 100
print(lista_numerica)
#print(lista[1])
#if 'lobo' in lista_animal:
 #   print('existe lobo na lista')
#else:
 #   print('não existe um lobo na lista')
  #  lista_animal.append('lobo')
   # print(lista_animal)