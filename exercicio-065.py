menor=maior=contador=soma=0
resposta= "S"
while resposta=="S":
    número = float(input('Digite um número:'))
    resposta = input('Quer continuar? [S/N]: ').upper().strip()[0]
    contador+=1
    soma+=número
    if contador ==1:
        maior = número
        menor = número

        soma += número
    elif contador>1:
        if número>maior:
            maior=número

            soma += número
        if número< menor:
            menor = número

            soma += número
    else:
        print('Valor inválido!')
print(f'Você digitou {contador} números, a soma foi de {soma} e  a sua média é de {soma/contador:.2f}, O maior valor digitado foi de {maior} e o menor valor digitado foi de {menor}.')
