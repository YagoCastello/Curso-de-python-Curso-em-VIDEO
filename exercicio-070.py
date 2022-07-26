count=menor=caro=total=0
barato=""
while True:
    nome=input("Digite o nome do produto:")
    preço=int(input("Digite o valor do produto em R$:"))
    total+=preço
    count+=1
    resp=input("Deseja continuar a comprando?[S/N]").upper().strip()
    if count==1:
        menor=preço
        barato=nome
    elif preço<menor:
        menor=preço
        barato=nome
    if preço>=1000:
        caro+=1
    if resp=="N":
        break
print(f" Você gastou no total {total}.\n Sendo que você comprou {caro}, produtos com o valor >=1000.\n O produto mais barato comprado foi {barato} por {menor} real(is).")
print(" Volte sempre")

