#frase=str(input("Digite uma frase:")).upper().strip()
#palavras=frase.split()
#junto= "".join(palavras)
#inverso = ""
#for letra in range(len(junto)-1,-1,-1):
#    inverso += junto[letra]
#if inverso == junto:
#    print("Temos um palíndromo!")
#else:
#    print("A frase digitada não é um palíndro!")
#print("{} , {}".format(junto,inverso))

###########################################################################################


#frase = input("Qual a frase? ").upper().replace(" ", "")
#if frase == frase[::-1]:
#    print("A frase é um palíndromo")
#else:
#    print("A frase não é um palíndromo")

#print(frase)
#print(frase[::-1])



############################################################################################


frase=str(input("Digite uma frase:")).upper().strip()
palavras=frase.split()
junto= "".join(palavras)
inverso = junto[::-1]
print("O inverso de {} é {}".format(junto,inverso))
if inverso == junto:
    print("Temos um palíndromo!")
else:
    print("A frase digitada não é um palíndro!")

