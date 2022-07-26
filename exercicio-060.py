"""

from time import sleep
print("Vamos fazer uma fatorial!")
x=int(input("Digite um número:"))
print("Calculando a fatorial de {}!".format(x))
sleep(1)
cont=1
while x!=0:
    if x !=0 and x!=1:
        cont= cont*x
        print("{} X ".format(x), end="")
        x -= 1
    elif x==1:
        cont = cont * x
        print("{}".format(x), end="")
        x -= 1
if x==0:
    print(" = ",end="")
print(cont)

"""



"""

from math import  factorial
n=int(input("Digite um número:"))
f=factorial(n)
print("O fatorial de {} é {}".format(n,f))

"""



num=int(input("Digite um número:"))
count=1
for c in range(num,0,-1):

    print("{}".format(num),end="")
    print("X"if num>1 else "=")
    count*=num
    num = num - 1
#print(num)
print(count)