count=0
from random import randint
print("Vamos jogar PAR ou ÍMPAR!")
while True:
    jogador=int(input("Digite um número:"))
    escolha=input("Qual a sua aposta [P/I]").strip().upper()
    pc=randint(1,10)
    print(f" Você jogou {jogador} e o pc jogou {pc}")
    soma=(jogador+pc)%2

    if soma == 0 and escolha == "I":
        print("Deu par. Você perdeu!")
        break
    elif soma==1 and escolha=="P":
        print("Deu ímpar. Você perdeu!")
        break

    if soma==0 and escolha=="P":
        count+=1
        print("Deu par. Você venceu!")

    elif soma==1 and escolha=="I":
        count+=1
        print("Deu ímpar. Você venceu!")
    #elif soma==1 and escolha=="P":
    #    print("Deu ímpar. Você perdeu!")
    else:
        print("Jogada inválida!")
print(f"Você venceu {count} vez(es) antes de perder.")

   # elif soma==0 and escolha=="I":
     #   print("Deu par. Você perdeu!")