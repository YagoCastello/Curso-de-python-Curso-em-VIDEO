x=int(input("Digite um número:"))
p=0
for c in range(1,x+1):
    if x%c==0:
        p+=1
        print("{}{}{}".format("\033[32;7m",c,"\033[m"))
    else:
        print("{}{}{}".format("\033[31m",c,"\033[m"))
if p==2:
    print("Como o valor {} só e divisivel por ele mesmo e por 1, ele é um número primo".format(x))
else:
    print("Como o valor {} é divisivel por ele mesmo e mais {} valores ele não é um número primo".format(x,p-1))
print(p)
