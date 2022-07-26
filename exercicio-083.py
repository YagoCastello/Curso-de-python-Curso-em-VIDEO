aberto=fechado=0
x=input("Digite uma expressão matemática:")
for c in range (0,len(x)-1):
    if c=="(":
        aberto+=1
    elif c==")":
        fechado+=1
if aberto==fechado:
    print("Você digitou uma expressão valida!")
else:
    print("Você digitou uma epressão inválida!")