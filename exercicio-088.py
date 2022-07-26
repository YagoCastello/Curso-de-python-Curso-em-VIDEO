from random import randint
megao=list()
mega=list()
total=0

resp=int(input("Quantos jogos você quer?"))
while total<resp:
    count = 0
    while True:
        num=randint(1,60)
        if num not in mega:
            mega.append(num)
            count+=1
        if count>=6:
            megao.append(mega[:])
            mega.clear()
            total+=1
            break

for c in range(0,resp):
    megao[c].sort()
    print(f"Jogo {c+1}º:{megao[c]}")