x=float(input('Nota da p1:'))
y=float(input('Nota da p2:'))
z=(x+y)/2
print("A sua nédia é {}".format(z))
if z >=7:
    print('{}Aprovado{}'.format("\033[1;32m",'\033[m'))
elif z<5:
    print('{}Reprovado{}'.format('\033[31;4m','\033[m'))
else:
    print("{}Recuperação{}".format("\033[35;1m",'\033[m'))