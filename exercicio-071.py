print("=" * 60)
print("{} Seja bem vindo ao banco Castello {}".format("=" * 10, "=" * 10))
print("=" * 60)
valor = int(input("Digite o valor que você quer sacar R$:"))
ced = 50
quantced = 0
total = valor
while True:
    if total >= ced:
        total -= ced
        quantced += 1
    else:
        if quantced > 0:
            print(" {} und de  R${},00".format(quantced, ced))
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        quantced=0
        if total == 0:
            break
print("Fim")