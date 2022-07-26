x1=int(input("Digite o primeiro número:"))
x2=int(input("Digite o segundo número:"))
print("""Escolha uma das opções abaixo:
 [1]Soma
 [2]Multiplicar 
 [3]Maior
 [4]Novos números
 [5]Sair do programa""")
escolha=int(input("Digite a sua opção:"))
while escolha !=5:
    print("""Escolha uma das opções abaixo:
     [1]Soma
     [2]Multiplicar 
     [3]Maior
     [4]Novos números
     [5]Sair do programa""")
    if escolha==1:
        print("A soma é entre {} e {} é {}".format(x1,x2,x1+x2))
    elif escolha==2:
        print("A multiplicação entre {} e {} é {}".format(x1,x2,x1*x2))
    elif escolha==3:
        if x1>x2:
            print(" {} é maior que {}".format(x1,x2))
        else:
            print(" {} é maior que {}".format(x2,x1))
    elif escolha==4:
        x1 = int(input("Digite o primeiro número:"))
        x2 = int(input("Digite o segundo número:"))
    else:
        print("Opção invalida. Tente novamente.")
    escolha=int(input("Digite a sua opção:"))
print("O programa foi finalizado com sucesso!")
print("fim")