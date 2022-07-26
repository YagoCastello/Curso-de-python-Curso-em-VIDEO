from math import sqrt
x=int(input('Digite um numero :'))
n=x**(1/2)
print(' O dobro é : {}{}{}\n O triplo é {}{}{} \n E a raiz quadrada é {}{}{}'.format('\033[1;34;45m',x*2,'\033[m','\033[4;37;41m',x*3,'\033[m','\033[4;31;45m',sqrt(x),'\033[m'))
