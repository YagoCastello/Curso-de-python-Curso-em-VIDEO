lista=[]
temp=[]
maior=menor=0
while True:
    temp.append(input("Digite o seu nome:"))
    temp.append(float(input("peso:")))
    resp=input("Deseja continuar?[s/n]:").strip().lower()[0]
    if len(lista)==0:
        maior=menor=temp[1]
    else:
        if temp[1]>maior:
            maior=temp[1]
        if temp[1]<menor:
            menor=temp[1]

    lista.append(temp[:])
    temp.clear()
    if resp=="n":
        break
print(lista)
print(f"O maior peso foi {maior}kg de :",end="")
for p in lista:
    if p[1]==maior:
        print(f"{p[0]}",end=" ")
print(f"\nO menor peso foi de {menor}kg",end="")
for p in lista:
    if p[1]==menor:
        print(f"{p[0]}",end=" ")