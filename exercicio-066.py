count=n=s=0
while True:
    n=int(input("Digite um valor . Caso queira parar digite 999:"))
    if n== 999:
        break
    count+=1
    s+=n
print(f"A soma do(s) termo(s) {count} , é igual a {s}")