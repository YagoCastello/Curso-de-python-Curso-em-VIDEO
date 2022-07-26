soma=0
for c in range(1,7):
    x=int(input("Digite o {}ª valor:".format(c)))
    if x%2!=0:
        soma +=x
print("A soma dos números impáres é {}".format(soma))