"""

numeros=("zero","um","dois","três","quatro","cinco","seis","sete","oito","nove",
         "dez","onze","doze","treze","catorze",
         "quinze","dezesseis","dezessete","dezoito","dezenove","vinte")

while True:
    x = int(input("Digite um valor entre 0 e 20 :"))
    if x <0 or x>20:
        print("Valor inválido, por favor digite um número válido:")
    else:
        print(numeros[x])
        resp=input("Quer continuar? S/N:").upper().strip()[0]
        if resp=="S":
            x = int(input("Digite um valor entre 0 e 20 :"))
        else:
            break
print(resp)

"""



"""
n = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if num < 0 or num > 20:
        print('Invalido Tente novamente ', end='')
    else:
        print(f'Você digitou o número {n[num]}')
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? S/N ')).upper().strip()[0]
    if resp == 'N':
        break
print('{:=^30}'.format(' PROGRAMA FINALIZADO '))


"""

n = ('zero', 'um', 'dois', 'três', 'quatro',
     'cinco', 'seis', 'sete', 'oito', 'nove',
     'dez', 'onze', 'doze', 'treze', 'quatorze',
     'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    x=int(input("Digite um valor de 0 a 20:"))
    if x<0 or x>20:
        print("Valor inválido.")
       # resp=input("quer tentar novamente?[S/N]:").strip().upper()[0]
    else:
        print(("você digitou {}{}{}".format("\033[31;4m",n[x],"\033[m")))
       # resp = input("quer tentar novamente?[S/N]:").strip().upper()[0]
    resp =" "
    while resp not in 'SN':
        #x = int(input("Digite um valor de 0 a 20:"))
        resp = input("quer tentar novamente?[S/N]:").strip().upper()[0]
    if resp=="N":
        break
print("fim!")