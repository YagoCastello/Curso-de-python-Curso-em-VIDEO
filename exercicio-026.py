x=str(input('Digite o seu nome:')).strip()
z= x.upper()
print('{}A letra A aparece {} vezes na frase{}'.format('\033[4;45;36m',z.count("A"),'\033[m'))
print('{}A primeira letra A apareceu na posição :{}'.format('\033[7;47;32m','\033[m'), z.find("A")+1)
print('{}A última letra A apareceu na posição :{}'.format('\033[1;44;31m','\033[m'), z.rfind("A")+1)

