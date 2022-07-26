par=soma=maior=0
matriz=[[0,0,0],[0,0,0],[0,0,0]]
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c]=(int(input(f"Digite um valor[{l}.{c}]:")))
        if matriz[l][c]%2==0:
            par+=matriz[l][c]
        if matriz[l][2]:
            soma+=matriz[l][2]
for c in range(0,3):
    if c==0:
        maior=matriz[1][c]
    elif matriz[1][c]>maior:
        maior=matriz[1][c]

for l in range(0,3):
    for c in range(0,3):
        print(f"[{matriz[l][c]:^5}]",end="")
    print()
print(f"O somatório dos valores pares foi {par}")
print(f"A soma da terceira coluna foi {soma}")
print(f"O maior valor da segunda linha é o {maior}")
