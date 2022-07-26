"""
total=[]
temp=[]
while True:
    nome=input("Digite o nome :")
    p1=float(input("Digite a p1:"))
    p2=float(input("Digite a p2:"))
    média=(p1+p2)/2
    temp.append(nome)
    temp.append(p1)
    temp.append(p2)
    temp.append(média)
    resp=input("Se não quer continuar digite 999:")
    total.append(temp[:])
    temp.clear()
    if resp =="999":
        break
print("=-"*30)
print("{:<10} {:<9} {:<20}".format("Nª","NOME","MÉDIA"))
for c in range(0,len(total)):
    if total[c][0]!="":
        print(f"{c:<10}",end="")
        print(f"{total[c][0]:<20}",end="")
        print(f"{total[c][3]:<10}")
pepete=input("Voqê quer ver a nota de algum aluno?[S/N]:")[0].upper().strip()
if pepete!="N":
    qaunt=int(input("Mostrar a nota de qual aluno?"))
    if qaunt==0 or qaunt<999:
        print(f"Nª{qaunt} Aluno(a): {total[qaunt][0]} p1: {total[qaunt][1]} p2:{total[qaunt][2]} média: {total[qaunt][3]} ")
print("programa finalizado")
"""

total=[]
temp=[]
while True:
    nome=input("Digite o nome :")
    p1=float(input("Digite a p1:"))
    p2=float(input("Digite a p2:"))
    média=(p1+p2)/2
    temp.append([[nome],[p1],[p2],[média]])
    #temp.append(p1)
    #temp.append(p2)
    #temp.append(média)
    resp=input("Se não quer continuar digite 999:")
    total.append(temp[:])
    temp.clear()
    if resp =="999":
        break
print("=-"*30)
print("{:<10} {:<9} {:<20}".format("Nª","NOME","MÉDIA"))
for c in range(0,len(total)):
    if total[c][0]!="":
        print(f"{c:<10}",end="")
        print(f"{total[c][0]:<20}",end="")
        print(f"{total[c][3]:<10}")
pepete=input("Voqê quer ver a nota de algum aluno?[S/N]:")[0].upper().strip()
if pepete!="N":
    qaunt=int(input("Mostrar a nota de qual aluno?"))
    if qaunt==0 or qaunt<999:
        print(f"Nª{qaunt} Aluno(a): {total[qaunt][0]} p1: {total[qaunt][1]} p2:{total[qaunt][2]} média: {total[qaunt][3]} ")
print("programa finalizado")
