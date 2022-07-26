x=float(input('Digite a velocidade do seu carro:'))
z=(x-80)*7
if x <=80.0:
    print('{}Diriga com cuidado.{}'.format('\033[1;32;46m','\033[m'))
else:
    print('Você será {}multado em {} reais {} por ultrapassar o limite de 80 km/h'.format('\033[1;32;46m',z,'\033[m'))