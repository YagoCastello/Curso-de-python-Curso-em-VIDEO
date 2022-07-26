import math
x=float(input('Digite um valor:'))
print(' valor digitado foi {}{}{} e o valor inteiro é {}{}{}'.format('\033[1;34;45m',x,'\033[m','\033[31;4;42m',math.trunc(x),'\033[m'))
