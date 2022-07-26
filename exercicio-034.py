x=float(input('Digite o seu salário que será reajustado:'))
if x <=1250:
    y=x*1.15
else:
    y=x*1.10
print('O seu novo salário é de {}R${:.2f} reais{}'.format('\033[1;32m',y,'\033[m'))