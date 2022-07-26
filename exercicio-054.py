import datetime
jovem=0
velho=0
y=datetime.date.today().year
for c in range (1,8):
    x=int(input("Digite em que ano a {}º pessoa nasceu:".format(c)))
    z=y-x
    if z<21:
        jovem+=1
    else:
        velho+=1
print("A {} jovem(ns) e {} velho(s)".format(jovem,velho))