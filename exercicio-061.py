print("Vamos fazer uma P.a com 10 termos, vamos começar.")
x=int(input("Digite o primeiro termo da P.A:"))
raz=int(input("Digite a razão da P.A:"))
an=0
vezes=1
while vezes!=11:
    an=x+(vezes-1)*raz
    vezes += 1
    print(an,"-> ",end="")
print("FIM!")
