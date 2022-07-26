import random
lista=[0,1,2,3,4,5,6,7,8,9,10]
pc=random.choice(lista)
erro=0
acertou=False
print("Vamos jogar um jogo... Eu pensei em um número de 0 a 10, tente adivinhar")
while acertou!=True:
    vc = int(input("Digite o seu palpite:"))
    if vc == pc:
        acertou = True
        erro += 1
        print("Parabéns você acertou!!!!, só gastou {} tentativa(s)".format(erro))
    elif vc>pc:
        print("Você errou! Tente um número menor.")
        erro += 1
    else:
        print("Você errou! Tente um número maior.")
        erro += 1
print("FIM!")
