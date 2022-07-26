import moedaNew

x = int(input('Digite um valor: R$ '))
porc = int(input('Digite quantos porcentos :'))

print(f'O dobro do valor {moedaNew.moeda(x)} é {moedaNew.dobro(x)}\nA metade de {moedaNew.moeda(x)} é {moedaNew.metade(x)}')
print(f'{moedaNew.moeda(x)} com um aumento de {porc}%, fica {moedaNew.aumento(x, porc)}')
print(f'{moedaNew.moeda(x)} com um redução de {porc}%, fica {moedaNew.diminuir(x, porc)}')
