tupla=("caderno",15.97,
       "Lápis",1.5,
       "Régua",2.35,
       "Grafite 0.7",2,
       "Tinta guache",5,
       "Mochila",59.60)
print("-"*40)
print(f"{'Loja Castello':^40}")
print("-"*40)
for pos in range(0,len(tupla)):
    if pos %2==0:
        print(f"{tupla[pos]:.<30}",end="")
    else:
        print(f" R$ {tupla[pos]:.>5.2f}")
print("-"*40)
