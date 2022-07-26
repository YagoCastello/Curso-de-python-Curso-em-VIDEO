s=0
d=0
for c in range(0,500,3):
    b = c % 2
    if b==1:
        s += c
        d +=b
print(d)
print("O somatorio dos  {} valores de 0 a 500 multiplos de 3 e que sejam impás , é igual a: {}".format(d,s))
print(s)

print("FIM")
