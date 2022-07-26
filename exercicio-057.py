sexo=input("Digite o seu sexo, F ou M:").upper()[0].strip()
while sexo not in "MmFf":
    sexo=str(input("Dados inválidos. Por favor digite o seu sexo: [M/F] ")).upper()[0].strip()
print(" O sexo digitado foi {}".format(sexo))
