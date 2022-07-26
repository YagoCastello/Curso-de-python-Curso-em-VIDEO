##############Minha-versão#############################
"""
lista = []
soma=media=0
while True:
    dicio = dict()
    dicio["nome"]=input("Digite o nome:")
    dicio["idade"]=int(input("Digite a idade:"))
    soma+=dicio["idade"]
    dicio["sexo"]=input("digiteo seu sexo[M ou F]:")[0].upper().strip()
    while dicio["sexo"] not in "MF":
        del (dicio["sexo"])
        print("Valor incorreto, por favor digite somente M ou F.")
        dicio["sexo"] = input("digite o seu sexo[M ou F]:")[0].upper().strip()
    resp=input("Quer continuar[S ou N]?")[0].upper().strip()
    while resp not in "SN":
        del(resp)
        print("Você digitou um valor inválido, por favor digite somente S ou N")
        resp = input("Quer continuar[S ou N]?")[0].upper().strip()
    lista.append(dicio.copy())
    del(dicio)
    if resp=="N":
        break
media=soma/len(lista[0])
print(f"Temos {len(lista[0])} pessoas cadastradas")
print(f'Soma das idade é {soma} e a média é {media:.2f}')
for p in lista:
    if p["sexo"]=="F":
        print(f' As mulheres cadastradas foram, {p["nome"]}',end="")
        print()
for p in lista:
    if p["idade"]>media:
        print(f'A idade de {p["nome"]} está acima da média.')

"""






galera=list()
pessoa=dict()
soma=média=0
while True:
    pessoa.clear()
    pessoa['nome']=str(input("Nome:"))
    while True:
        pessoa["sexo"]=str(input("Sexo: [M/F] "))[0].upper().strip()
        if pessoa["sexo"] in "MF":
            break
        print("ERRO! Por favor, digite apenas M ou F.")
    pessoa["idade"]=int(input("idade: "))
    soma+=pessoa["idade"]
    galera.append(pessoa.copy())
    while True:
        resp=str(input("Quer continuar? [S/N]:"))[0].strip().upper()
        if resp in "SN":
            break
        print("ERRO! Responda apenas S ou N.")
    if resp=="N":
        break
print("-="*30)
print(f"A) Ao todo temos {len(galera)} pessoas cadastradas.")
média=soma/len(galera)
print(f"B) A média de idade é de {média:5.2f} anos.")
print("C) As mulheres cadastradas foram ",end="")
for p in galera:
    if p["sexo"] in "Ff":
        print(f"{p['nome']} ",end="")
print()
print('D) Lista das pessoas que estão acima da média: ')
for p in galera:
    if p['idade']>=média:
        print("     ")
        for k, v in p.items():
            print(f" {k} = {v};",end="")
        print()
print("<< ENCERRADO >>")