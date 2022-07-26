from datetime import date
x=date.today().year
trabalho=dict()
trabalho["nome"]=input("nome:")
trabalho["ano-nasc"]=int(input("Ano de nascimento:"))
trabalho["carteira-trab"]=int(input("Nº carteira de trabalho(0 sem carteira de trabalho):"))
trabalho["idade"]=x-trabalho["ano-nasc"]
if trabalho["carteira-trab"]!=0:
    trabalho["ano-de-contratação"]=int(input("Ano de contratação:"))
    trabalho["Salário"]=float(input("Salário:"))
print("-="*30)
for k, v in trabalho.items():
    print(f"{k} é igual {v}")
if trabalho["carteira-trab"] != 0:
    print(f'A aposentadoria tem o valor de {trabalho["idade"] + (trabalho["ano-de-contratação"] + 35) - x}')

