def aumentar(preço = 0, taxa=0, formato= False):
    res = preço + (preço * taxa/100)
    return res if formato == False else moeda(res)


def diminuir(preço=0, taxa=0, formato=False):
    res = preço - (preço * taxa/100)
    return res if formato == False else moeda(res)


def dobro(preço=0, formato=False):
    res = preço * 2
    return res if formato ==  False else moeda(res)


def metade(preço=0, formato=False):
    res = preço/2
    return res if formato == False else moeda(res)


def moeda(preço=0, moeda="R$", formato=False):
    return f'{moeda} {preço:>.2f}'.replace('.', ',')


def resumo(preço=0, aumento=10,diminui=5):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço,True)}')
    print(f'Metade do preço: \t{metade(preço,True)}')
    print(f'{aumento}% de aumento: \t{aumentar(preço,aumento,True)}')
    print(f'{diminui}% de aumento: \t{diminuir(preço,diminui,True)}')
    print('-'*30)
