x=float(input('Digite o primeiro numero:'))
y=float(input('Digite o segundo numero:'))
z=float(input('Digite o terceiro numero:'))
if x>y and x>z:
    maior=x
if y>x and y>z:
    maior=y
if z>x and z>y:
    maior=z
if x<y and x<z:
    menor=x
if y<x and y<z:
    menor=y
if z<x and z<y:
    menor=z
print("O maior valor é o {}{}{}".format('\033[4;32;46m',maior,'\033[m'))
print('E o menor valor é o {}{}{}'.format('\033[1;33;46m',menor,'\033[m'))