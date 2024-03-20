atual = int(input('em qual ano estamos? :'))
nasc = int(input('em qual ano vc nasceu? :'))
conta = atual - nasc
if conta >= 18:
    print('parabes vc ja pode ser preso :) !!!!kakkakkaakk')
else:
    print('vc nasceu em {} e tem {} ANOS DE idade'.format(nasc, conta))