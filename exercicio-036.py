s=float(input('Quanto é o seu salário ?'))
v=float(input('Qual é o valor do imóvel ?'))
ano=int(input('Em quantos anos pretende pagar a casa ?'))
parc=v/ano
mes=parc/12
print('A prestação da casa é de {:.2f} e você ganha {}'.format(mes,s))
print('O minimo a ser pago é de {:.2f} e você pode pagar até {:.2f} '.format(mes,0.3*s))
if mes> s*0.3:
    print('O seu empréstimo foi {}recusado{}'.format('\033[4;31m','\033[m'))
else:
    print('Seu empréstimo foi {}aprovado{}'.format('\033[1;32m','\033[m'))
