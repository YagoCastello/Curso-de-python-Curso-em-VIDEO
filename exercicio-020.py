import random
x = input('Digite o nome do 1º aluno :')
y = input('Digite o nome do 2º aluno :')
w = input('Digite o nome do 3º aluno :')
z = input('Digite o nome do 4º aluno :')
lista=[x,y,w,z]
random.shuffle(lista)
print("A ordem dos alunos é {}{}{}".format('\033[1;32;46m',lista,'\033[m'))