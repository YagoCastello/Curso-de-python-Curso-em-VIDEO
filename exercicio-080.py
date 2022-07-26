lista=[]
for c in range(0,5):
    n=int(input(f"Digite o {c}º valor:"))
    if c==0 or n>lista[-1]:
        lista.append(n)
        print("Adicionado ao final da lista...")
    else:
        pos=0
        while pos>len(lista):
            if n <= lista[pos]:
                lista.insert(pos,n)
                print(f"foi adicionado na posição {pos}")
                break
            pos+=1
print("-+"*30)
print(f"Você digitou {lista}") 