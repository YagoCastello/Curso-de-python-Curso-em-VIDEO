"""

alunos={}
lista=list()
alunos["nome"]=input("digite um nome:")
alunos["média"]=float(input("digite a média:"))
if alunos["média"]<5:
    alunos["situação"]="reprovado"
elif 5<=alunos["média"]<7:
    alunos["situação"]="recuperação"
else:
     alunos["situação"]="aprovado"
print("-="*30)
for k,v in alunos.items():
    print(f" -{k} é igual a {v}")
"""
while True:
    alunos={}
    lista=list()
    count=0
    print(f"Aluno {count}º")
    alunos["nome"]=input("digite um nome:")
    alunos["média"]=float(input("digite a média:"))
    resp=input("Deseja continuar?[S/N]:")[0].lower().strip()
    if resp!="n":
        if alunos["média"]<5:
            alunos["situação"]="reprovado"
        elif 5<=alunos["média"]<7:
            alunos["situação"]="recuperação"
        else:
             alunos["situação"]="aprovado"
        print("-="*30)
        for k,v in alunos.items():
            print(f" -{k} é igual a {v}")
    count+=1
    if resp=="n":
        break
x=int(input("Digite o numero do aluno:"))
print(lista[x])


