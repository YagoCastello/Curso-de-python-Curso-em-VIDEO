#
# MINHA VERSÃO
# def area():
#     s = a*b
#     print(f' {a} x {b} equivale a uma area de {s}')
#
#
# a = float(input('Digite a altura: '))
# b = float(input('Digite a largura: '))
# area()

# VERSÃO DO GUANABARA
#
def área(larg, comp):
    a = larg * comp
    print(f'A área de um terreno  {larg} X {comp} é de {a} m².')


#PROGRAMA PRINCIPAL
print('Controle de Terrenos')
print('-'*20)
l = float(input('LARGURA (m):'))
c = float(input('COMPRIMENTO (m): '))
área(l, c)
