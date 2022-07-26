x=count=p=0
x=int(input("Digite um valor , para parar digite 999:"))
while x !=999:
    count+=1
    p+=x
    x = int(input("Digite um valor , para parar digite 999:"))
print("Você digitou {} número(s) e a soma é igual {}".format(count,p))