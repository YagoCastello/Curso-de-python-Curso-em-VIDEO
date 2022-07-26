valores=(int(input("Digite um número:")),
             int(input("Digite um número:")),int(input("Digite um número:")),int(input("Digite um número:")))
nove=pares=0
for n in valores:
    if n==9:
        nove+=1
    elif n%2==0:
        pares+=1
print(f"O valor 9 apareceu {nove} vez(es) \nExiste {pares} número(s) par(es) ")
if 3 in valores:
    print(f"A primeira aparição do 3 é na posição {valores.index(3)+1}")
else:
    print(f"O número 3 não foi digitado em lugar nenhum")