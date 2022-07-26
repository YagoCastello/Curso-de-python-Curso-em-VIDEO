x = int(input('Digite um numero:'))
n = x + 1
a = x - 1
cores = {'limpa':'\033[m','azul':'\033[1;36m','vermelho':'\033[31m','magenta':'\033[35m'}
print('O sucessor do numero {}{}{} é o {}{}{} e o seu antecessor é o {}{}{}'.format(cores['vermelho'],x,cores['limpa'],cores['magenta'],n,cores['limpa'],cores['azul'],a,cores['limpa']))
