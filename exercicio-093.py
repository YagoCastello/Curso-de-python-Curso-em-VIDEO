dicio=dict()
lista=list()
soma=0
dicio["Jogador"]=input("Nome do jogador:")
dicio["Partidas"]=int(input("Quantas partidas o jogador participou:"))
dicio["gols"]=lista
for c in range(1,dicio["Partidas"]+1):
    lista.append(int(input(f"Quantos gols foram feitos no {c}º jogo:")))
dicio["total"]=sum(lista)
print("=-"*30)
print(dicio)
print("=-"*30)
for k,v in dicio.items():
    print(f"{k} = {v}")
print("=-"*30)
print(f'O jogador {dicio["Jogador"]} jogou {dicio["Partidas"]} partidas')
for c in range(0,dicio["Partidas"]):
    print(f'=> Na partida {c+1}ª, fez {dicio["gols"][c]} ')
print(f'Fazendo num total de {dicio["total"]}')