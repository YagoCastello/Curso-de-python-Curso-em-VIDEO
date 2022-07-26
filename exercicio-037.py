x=int(input('Digite um numero inteiro:'))
print('''Escolha a forma de conversão abaixo:
[1] para converter em BINÁRIO
[2] para converter em OCTAL
[3] para converter em HEXADECIMAL''')
y=int(input('Digite o número referente a conversão desejada :'))
if y==1:
    print('O número {} em Binário é {}'.format(x,bin(x)[2:]))
elif y==2:
    print('O número {} em Octal é {} '.format(x,oct(x)[2:]))
elif y==3:
    print('O número {} em Hexadecimal é {}'.format(x,hex(x)[2:]))
else:
    print('{}Opção inválida{}. Por favor tente novamente'.format('\033[31;4m','\033[m'))
