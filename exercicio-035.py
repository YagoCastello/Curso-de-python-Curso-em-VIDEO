print("-=-"*10)
print('Vamos analisar os segmentos para formar um triangulo')
x=float(input('Digite o primeiro segmento :'))
y=float(input('Digite o segundo segmento:'))
z=float(input('Digite o terceiro segmento:'))
if x <y+z and y<x+z and z<x+y:
    print("Os segmentos {}formam um triangulo{}".format('\033[32m','\033[m'))
else:
    print('Os segmentos {}NÃO formam um triangulo{}'.format('\033[31m','\033[m'))
print("-=-"*10)