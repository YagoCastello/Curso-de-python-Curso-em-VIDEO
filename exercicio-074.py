from random import randint
valores=(randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10))
print("Os valores sorteados foram:", end="")
for n in valores:
    print(f"{n} ",end="")
print(f"\nOs valores sorteados foram {valores}. E o maior valor foi {max(valores)} .E o menor valor foi {min(valores)}")
