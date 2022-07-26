# #VERSÃO GUANABARA
#
# def leiaInt(msg):
#     ok = False
#     valor = 0
#     while True:
#         n = str(input(msg))
#         if n.isnumeric():
#             valor = int(n)
#             ok = True
#         else:
#             print('\033[0;31mErro! Digite um número inteiro válido.\033[m')
#         if ok:
#             break
#     return valor


#PROGRAMA PRINCIPAL

# n = leiaInt("Digite um número: ")
# print(f'Você acabou de digitar o número {n}')


#MINHA VERSÃO BY YAGO
def leiaInt(msg):
    valor = 0
    while True:
        n = input(msg)
        if n.isnumeric():
            valor = int(n)
            break
        else:
            print('\033[4;33mERRO! VALOR INVÁLIDO! Digite um número:\033[m ')
    return valor


#PROGRAMA PRINCIPAL
n = leiaInt("Digite um número: ")
print(f'Você acabou de digitar o número {n}')
