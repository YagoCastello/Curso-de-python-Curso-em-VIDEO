x=float(input('Digite qual é a distância da sua viagem?'))
#if x<=200:
   # print('O preço da sua passagem é de R${} reais. '.format(x*0.5))
#else:
   # print('O preço da sua passagem é de R${} reais. '.format(x*0.45))
preco = x * 0.5 if x <= 200 else  x * 0.45
print(f'\033[31;42m ' + f'O preço da sua viagem é de {preco}' +f'\033[m')