x=int(input("Digite a idade do atleta:"))
if x <=9:
    print("MIRIM")
elif x>9 and x<=14:
    print("INFANTIL")
elif x>14 and x<=19:
    print("JUNIOR")
elif x>19 and x<=20:
    print("SÊNIOR")
else:
    print("MASTER")