x=input('Qual é o nome?').strip()
print('O seu nome é {}{}{}, e em maíusculo é {}{}{}'.format('\033[4;32;46m',x,'\033[m','\033[7;32;45m',x.upper(),'\033[m'))
print('O seu nome é {}{}{}, e em minusculo é {}{}{}'.format('\033[1;33;47m',x,'\033[m','\033[7;31;46m',x.lower(),'\033[m'))
print('O seu nome ao todo tem {}{}{} letras'.format('\033[4;31;46m',len(x)-x.count(' '),'\033[m'))
y=x.split()
print(len(y[0]))