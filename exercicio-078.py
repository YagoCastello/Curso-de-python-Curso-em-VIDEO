#x=int(input("aaa"))
menor=maior=p=q=0
lista=[]
maio=[]
meno=[]
for c in range(1,6):
    x = int(input(f"Digite o {c}º de 5:"))
    lista.append(x)
    if c ==1:
        maior=x
        menor=x
    elif x>maior:
        maior=x

    elif x<menor:
        menor=x
for c, v in enumerate(lista):
    if v==maior:
        maio.append(c+1)
    if v==menor:
        meno.append(c+1)

print(lista)
print(f"o maior foi {maior} em {maio}")
print(f"o menor foi {menor} em {meno}")

