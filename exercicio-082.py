lista=[]
par=[]
impar=[]
while True:
    x=int(input("Digite um valor:"))
    resp=input("Deseja continuar?[S/N]")
    lista.append(x)
    if x%2==0:
        par.append(x)
    else:
        impar.append(x)
    if resp in "Nn":
        print("Programa finalizado...")
        print(f"você digitou  os seguintes valores: {lista}")
        print(f"Sendo {par} os pares")
        print(f"Sendo {impar} os ímpares")
        break