lista=[]
count=0
while True:
    lista.append(int(input("Digite um valor:")))
    resp=input("Você quer continuar?[S/N]").lower().strip()[0]
    count+=1
    if resp=="n":
        break
if 5 in lista:
    print("O número 5 aparece na lista")
else:
    print("O valor 5 não aparece na lista.")
lista.sort(reverse=True)
print(f"Você digitou os seguintes valores {lista}.")
print(f"Você digitou {count} termo(s).")
