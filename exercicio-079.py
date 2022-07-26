lista=[]
while True:
    x=int(input("Digite um valor:"))
    if x not in lista:
        lista.append(x)
        print("Valor adicionado com sucesso...")
    else:
        print("Valor duplicado!Não vou adicionar.")
    resp = input("Quer continuar?").strip()[0]
    if resp in "Nn":
        break
lista.sort()
print(f"Você digitou os seguintes valores : {lista}")

