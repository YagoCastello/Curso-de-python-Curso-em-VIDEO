print("Vamos fazer uma P.a com 10 termos, vamos começar.")
x=int(input("Digite o primeiro termo da P.A:"))
raz=int(input("Digite a razão da P.A:"))
an=0
vezes=1
mais=10
total=0
while mais !=0:
    total=total+mais
    while vezes<=total:
        an=x+(vezes-1)*raz
        vezes += 1
        print(an,"-> ",end="")
    print("PAUSA")
    mais=int(input("Quantos termos você quer mostrar a mais:"))
print("A progressão tem {} termos".format(total))
