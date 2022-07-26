import random
x=input('Digite o nome do primeiro aluno:')
y=input("Digite o nome do segundo aluno:")
z=input('Digite o nome do terceiro aluno:')
w=input('Digite o nome do quarto aluno:')
lista= [x,y,z,w]
escolhido=random.choice(lista)
print('O aluno(a) escolhido(a)  foi o(a) {}{}{}'.format('\033[4;32;47m',escolhido,'\033[m'))
#print(f'O aluno(a) escolhido(a)  foi o(a) {escolhido}')
#print('O aluno(a) escolhido(a)  foi o(a) ',random.choice(lista))
