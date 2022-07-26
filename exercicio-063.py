
"""
res=int(input("Digite um número:"))
count=1

antes=0
depois=1
fibo=depois+antes
while count<=res:
    print(fibo)
    antes=fibo
    depois=
    count+=1
print("fim")
"""


n=int(input("Deseja ver quantos termos da sequência de fibonati?"))
t1=0
t2=1
t3=t1+t2
count=3
print("{} -> {} ->".format(t1,t2),end="")
while count!=n:
    print("  {} ->".format(t3),end="")
    t1=t2
    t2=t3
    t3=t1+t2
    count+=1
print("Fim")

