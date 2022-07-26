# #Versão Guanabara
#
# from time import sleep
#
#
# def maior(*núm):
#     cont = maior = 0
#     print('-='*30)
#     print('Analisando os valores passados...')
#     for valor in núm:
#         print(f'{valor} ', end='', flush=True)
#         sleep(0.3)
#         if cont == 0:
#             maior = valor
#         else:
#             if valor > maior:
#                 maior = valor
#         cont += 1
#     print(f'Foram informados {cont} valores ao todo.')
#     print(f'O maior valor informado foi {maior}.')
#
#
# #Programa principal
# maior(2, 9, 4, 5, 7, 1)
# maior(4, 7, 0)
# maior(1, 2)
# maior(6)
# maior()
#

#Minha Versão

def funcao(list):
    print('=-'*40)
    print(f'Analisando os valores passados ....')
    for k, v in enumerate(list):
        print(f'{v} ', end=" ")
    print(f" Foram informados {len(list)} valores ao todo. ")
    print(f'O maior valor informado foi de {max(list)}. ')


lista = [7, 8, 45, 3, 9]
ba = [4, 69, 3, 2]
pi = [3, 14]
funcao(lista)
funcao(ba)
funcao(pi)
