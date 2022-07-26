import random
from time import sleep
x=str(input(" Vamos jogar joken po, escolha entre pedra , papel ou tesoura \n Digite a sua escolha aqui:")).lower().strip()
lista=["pedra","papel","tesoura"]
comp=random.choice(lista)
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!!!!")
sleep(1)
print("O computador jogou {}".format(comp))
if x==comp:
    print("Deu empate!")
elif x== "pedra" and comp =="tesoura":
    print("Você venceu!")
elif x== "pedra" and comp=="papel":
    print("O computador venceu!")
elif x=="papel" and comp=="tesoura":
    print("O computador venceu!")
elif x=="papel" and comp =="pedra":
    print("Você venceu!")
elif x=='tesoura' and comp=="papel":
    print("Você venceu!")
elif x=="tesoura" and comp=="pedra":
    print("O computador venceu!")
else:
    print("{}Opção inválida!{}".format("\033[31;7;m","\033[m"))
