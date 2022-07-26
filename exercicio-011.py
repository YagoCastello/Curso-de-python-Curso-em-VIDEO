x=float(input('Digite a largura da parede:'))
y=float(input('Digite a altura da parede:'))
a=x*y
tinta= a/2
print('Area é de {}{:.2f}{}  m2 e será necessario {}{:.2f}{} L de tinta'.format('\033[1;32;46m',a,'\033[m','\033[4;32;45m',tinta,'\033[m'))