x=float(input('Digite o primeiro número:'))
y=float(input('Digite o segundo número:'))
if x>y:
    print('O {}primeiro número{} , é o maior entre os dois'.format('\033[4;31;47m','\033[m'))
elif y>x:
    print('O {}segundo número{} , é o maior entre os dois'.format('\033[7;35;42m','\033[m'))
else:
    print('{}Os dois números são iguais{}'.format('\033[31;2;44m','\033[m'))
