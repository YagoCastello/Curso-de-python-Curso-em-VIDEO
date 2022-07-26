from random import randint
from time import sleep
from operator import itemgetter
dados={"Jogador 1":randint(1,6),
       "Jogador 2":randint(1,6),
       "Jogador 3":randint(1,6),
       "Jogador 4":randint(1,6)}
rankin=[]
for k , v in dados.items():
    print(f"O {k} tirou {v}")
    sleep(1)
rankin=sorted(dados.items(),key=itemgetter(1),reverse=True)
for i, v in enumerate(rankin):
    print(f"O {i+1}º lugar: {v[0]} com {v[1]}")