
veio=""
maior=0
menor=0
soma=0
for c in range(1,5):
    nome=input("Digite o nome da {}ª pessoa:".format(c)).strip()
    sexo=input("Digite o sexo da pessoa, usando F para feminino ou M para masculino:").upper().strip()
    idade=int(input("Digite a idade:"))
    soma+=idade
    if c==1:
        maior=idade

    else:
        if idade>maior and sexo=="M":
            maior=idade
            veio=nome
        if idade<20 and sexo=="F":
            menor+=1
media=soma/4
print("O homem mais velho  é {} com {} anos".format(veio,maior))
print("Há {} mulher(es) com menos de 20 anos".format(menor))
print("E a média de idade é {}".format(media))