#Versão Guanabara
# from time import sleep
#
#
# def contador(i, f, p):
#     if p < 0:
#         p *= -1
#     if p == 0:
#         p = 1
#     print('-='*20)
#     print(f'Contagem de {i} até {f} de {p} em {p}')
#     sleep(2.5)
#
#     if i < f:
#         cont = i
#         while cont <= f:
#             print(f' {cont} ', end="", flush=True)
#             sleep(0.5)
#             cont += p
#         print('FIM!')
#     else:
#         cont = i
#         while cont >= f:
#             print(f' {cont} ', end='', flush=True)
#             sleep(0.5)
#             cont -= p
#         print('FIM!')
#
#
# contador(1, 10, 1)
# contador(10, 0, 2)
# print('-='*20)
# print('Agora é sua vez de personalizar a contagem!')
# ini = int(input('Início: '))
# fim = int(input('Fim:    '))
# pas = int(input('Passo:  '))
# contador(ini, fim, pas)

#Minha versão

def contador(ini, fim, passo):

    print(f'Contagem de {ini} até {fim} em {passo}')
    print(f'=-' * 30)
    print(f'{ini}', end=" ")
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo += 1
    while True:
        if ini < fim:
            ini += passo
            if ini > fim:
                print(f' ')
                print(f'=-'*30)
                break
            if ini == fim:
                print(f' {ini} ', end='')
                print(' FIM!')
                print(f'=-' * 30)
                break
            else:
                print(f' {ini} ', end=" ")

        if ini > fim:
            ini -= passo
            if ini < fim:
                print(' FIM!')
                print(f'=-' * 30)
                break
            if ini == fim:
                print(f' {ini} ', end='')
                print(' FIM!')
                print(f'=-' * 30)
                break
            else:
                print(f' {ini} ', end=" ")


contador(1, 10, 1)
contador(10, 0, 2)
contador(12, -10, 7)
contador(15, -7, 0)
