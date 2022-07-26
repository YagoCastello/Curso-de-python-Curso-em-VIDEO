print("{:=^40}".format(" Lojas Castello "))
x=float(input("Digite o valor do produto R$:"))
print("""Escolha uma das formas de pagamento abaixo
 [1] dinheiro ou cheque-10% de desconto
 [2] A vista no cartão-5% de desconto
 [3] 2x no cartão-preço normal
 [4] 3x mais no cartão-20% de juros
""")
y=int(input("Digite a sua escolha: "))
if y==1:
    print("O valor á ser pago é de {}".format(x*0.9))
elif y==2:
    print("O valor vai ser de {}".format(x*0.95))
elif y==3:
    print("O valor é {}".format(x))
else:
    print("O valor é de {} ".format(x*1.2))