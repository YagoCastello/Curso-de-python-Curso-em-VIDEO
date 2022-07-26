r1=float(input("Digite o primeiro segmento de reta:"))
r2=float(input("Digite o segundo segmento de reta:"))
r3=float(input("Digite o terceiro segmento de reta:"))
if r1<r2+r3 and r2<r1+r3 and r3<r2+r1:
    print("Esses segmentos PODEM formar um triangulo.",end="")
    if r1 == r2 == r3:
        print("EQUILATERO!")
    elif r1 != r2 and r1 !=r3 and r2 != r3:
        print("ESCALENO!")
    else:
        print("ISÓCELES!")
else:
    print("NÃO FORMAM UM TRIANGULO")
