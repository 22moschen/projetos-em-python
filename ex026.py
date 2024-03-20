frase = str(input('Digite uma frase ')).strip()
print('a letra [a] aparece {} vezes ' .format(frase.count('a')))
print('a letra [a] apareceu na posição {} ' .format(frase.find('a')+1))
print('a ulltima aparição de [a] é na posição {} kkkk'.format(frase.rfind('a')+1))