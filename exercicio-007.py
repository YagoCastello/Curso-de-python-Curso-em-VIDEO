n1 = float(input('Digite a nota da p1:'))
n2 = float(input('Digite a nora da p2:'))
m = (n1+n2)/2
#print( 'A media do aluno(a) é {}{:.2f}{}'.format('\033[1;32;45m',m,'\033[m'))
if m>=6:
    print('Você está {}{}{} '.format('\033[1;32m','Aprovado','\033[m'))
else:
    print('Você está {}{}{}'.format('\033[1;31m','Reprovado','\033[m'))
