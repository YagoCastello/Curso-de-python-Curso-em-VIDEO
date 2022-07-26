x=int(input('Digite um numero qualquer:'))
z=x%2
if z==0:
    print('O numero {} é {}PAR!{}'.format(x,'\033[4;32;47m','\033[m'))
else:
    print('O numero {} é {}ÍMPAR{}'.format(x,'\033[4;33;45m','\033[m'))