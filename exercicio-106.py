def ajuda(n):
    help(n)

while True:
    print(f'\033[38;4;47m')
    resp = input('Função ou Biblioteca:')
    print('\033[m')
    if resp == "FIM":
        print(f'\033[36;4;45m')
        print('Até logo!')
        print('\033[m')
        break
    else:
        print(f'\033[31;4;42m')
        maria = ajuda(resp)
        print('\033[m')
