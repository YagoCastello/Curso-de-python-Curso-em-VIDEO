import datetime
a=int(input("Em que ano você nasceu?"))
x=int(input("""Qual é o seu sexo? por favor responda com 
[1] para feminino 
[2] para masculino
Digite a sua resposta:"""))
y=datetime.date.today().year
idade=y-a
p=18-idade
k=idade-18
if x ==1:
    print("A senhorita, não é obrigada a se alistar. Mas caso queira pode se alistar, responda com sim ou não : ")
    z=str(input("Qual é a sua decisão?")).strip().lower()
    if z == "sim":
        print("Vamos ver conferir se a senhorita tem a idade correta.")
        if z == "sim" and idade == 18:
            print("Está na idade de se alistar")
        elif z == "sim" and idade <18:
            print("Você tem {} e falta {} para se alistar.Você deve se alistar no ano {}".format(idade,p,p+y))
        elif z == "sim" and idade >18:
            print("Você tem {} anos e já passou {} anos desde a epóca correta do seu alistamento . Que foi no ano de {}".format(idade,k,y-k))
    elif z== "não":
        print("Tudo bem , tenha um bom dia!")

elif x == 2:
    print("Vamos verificar se você está na idade correta ....")
    if idade ==18:
        print("Seja bem vindo ao exercito!")
    elif idade <18:
        print("Você tem {} anos e te falta {} ano(s) para se alistar , volte em {}".format(idade,p,y+p))
    elif idade>18:
        print("Você tem {} anos e já se passaram {} ano(s) do seu alistamento obrigatório, que foi no ano de {} ".format(idade,k,y-k))
else:
    print("Opção inválida")