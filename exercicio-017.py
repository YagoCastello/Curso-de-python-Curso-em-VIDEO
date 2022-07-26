import math
x=float(input('Digite o angulo do cateto adjacente:'))
y=float(input('Digite o angulo do cateto oposto:'))
h= math.sqrt(x**2 + y**2)
print(' O valor da hipotenusa é {}{:.2f}{}'.format('\033[4;33;46m',h,'\033[m'))