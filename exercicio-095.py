"""

A=list()
while True:
    Bjogador=dict()
    gols=[]
    soma=0
    Bjogador["nome"]=input("nome:")
    Bjogador["partidas"]=int(input("Quantas partidas ele(a) jogou?"))
    for c in range(1,(Bjogador["partidas"])+1):
        gols=int(input(f"Quantos gols no {c}ª jogo:"))
        soma+=gols
        A.append(gols)
    Bjogador["gols"]=gols[:]
    A.append(Bjogador.copy())
    A.append(soma)
    continuar=input("Você quer continuar? [S/N]:")[0].strip().upper()
    if continuar=="N":
        break

print("=-"*45)
print(f"{'Cod  nome':<20}{'gols':<15}{'Total':<15}")
for c in range(0,len(A)):
    print(f'{c}  {soma}')
"""

"""
lista=list()

while True:
    gols=list()
    dicio=dict()
    soma=0
    dicio["Jogador"]=input("Nome do jogador:")
    dicio["Partidas"]=int(input("Quantas partidas o jogador participou:"))
    dicio["gols"]=gols
    for c in range(1,dicio["Partidas"]+1):
        x=int(input(f"Quantos gols foram feitos no {c}º jogo:"))
        soma+=x
        gols.append(x)
    #dicio["total"]=sum(lista)
    lista.append(dicio.copy())
    resp=input("Você quer continuar? [S/N]:")[0].strip().upper()
    if resp=="N":
        break
print("=-"*30)
print(dicio)
print("=-"*30)
for k,v in dicio.items():
    print(f"{k} = {v}")
print("=-"*30)
print(f'O jogador {dicio["Jogador"]} jogou {dicio["Partidas"]} partidas')
for c in range(0,dicio["Partidas"]):
    print(f'=> Na partida {c+1}ª, fez {lista} ')
print(f'Fazendo num total de {soma}')

"""


"""

time=list()
jogador=dict()
partidas=list()

while True:
    jogador.clear()
    jogador["nome"]=str(input("Digite o nome:"))
    tot=int(input(f'Digite o total de partidas que {jogador["nome"]} jogou:'))
    partidas.clear()
    for c in range(0,tot):
        partidas.append(int(input(f"Quantos gols no {c+1} ª jogo:")))
    jogador["gols"]=partidas[:]
    jogador["total"]=sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]')).upper()[0]
        if resp in "SN":
            break
        print('ERRO! Responda apenas S ou N.')
    if resp =="N":
        break
print("-="*30)
print("cod",end="")
for i in jogador.keys():
    print(f"{i:<15}  ",end="")
print()
print("-"*40)
for k, v in enumerate(time):
    print(f"{k:>3}",end="")
    for d in  v.values():
        print((f"{str(d):<15}"),end="")
    print()
print("-"*40)
while True:
    busca=int(input("Mostrar dados de qual jogador? (999 para parar)"))
    if busca ==999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com o código {busca}')
    else:
        print(f'--LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'     No jogo {i+1} fez {g} gols.')
    print("-"*40)
print("<< VOLTE SEMPRE >>")
"""



nome="walter"
nome=input("nome:")
print(nome)




