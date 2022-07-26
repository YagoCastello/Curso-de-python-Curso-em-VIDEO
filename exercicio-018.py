import math
x=float(input('Digite um angulo:'))
y=math.sin(math.radians(x))
z=math.cos(math.radians(x))
w=math.tan(math.radians(x))
print('O angulo de {}{}{} tem : \n SENO = {}{:.2f}{} \n COSSENO = {}{:.2f}{} \n TANGENTE = {}{:.2f}{}'.format('\033[4;32;46m',x,'\033[m','\033[7;47;31m',y,'\033[m','\033[4;46;32m',z,'\033[m','\033[1;35;42m',w,'\033[m'))