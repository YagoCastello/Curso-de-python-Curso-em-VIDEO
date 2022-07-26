import random
x=[0,1,2,3,4,5]
z=random.choice(x)
print('-=-'*17)
p=input("Vou pensar em um numero de 0 a 5. Tente adivinhar :")
print("Processando ....")
if p==z:
    print('Meus parabens você {}ACERTOU!{}'.format('\033[1;45;32m','\033[m'))
else:
    print('Você {}ERROU!{} eu pensei no numero {} e não no {}'.format('\033[4;46;31m','\033[m',z,p))
print('-=-'*18)
