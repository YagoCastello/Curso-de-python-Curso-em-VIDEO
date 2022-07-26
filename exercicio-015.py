x = float(input('Digite quantos quilometros foram percorridos:'))
y= int(input('Digite quantos dia ficou com o carro alugado:'))
c= x*0.15+y*60
print('O seu gasto foi de R${}{:.2f}{}'.format('\033[7;42;36m',c,'\033[m'))
