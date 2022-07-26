"""
lista=[[],[],[]]
for pri in range(0,3):
    for c in range(0,3):
        lista[pri].append(int(input(f"digite um valor para {pri}.{c}:")))
for pri in range(0,3):
    for c in range(0,3):
        print(f"[{lista[pri][c]:^5}]",end="")
    print()

"""

matriz=[[0,0,0],[0,0,0],[0,0,0]]
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c]=int(input(f"Digite o valor [{l},{c}]:"))
for l in range(0,3):
    for c in range(0,3):
        print(f"[{matriz[l][c]:^5}]",end="")
    print()