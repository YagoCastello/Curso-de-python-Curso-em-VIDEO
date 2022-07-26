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






#
# def resumo(preço=0, aumento=0, diminuir=0):
#     print('-=' * 45)
#     print(f'O preço analisado:      R$ {preço}')
#     print(f'O Dobro  do preço:      {preço*2}')
#     print(f'A metade do preço:      {preço/2}')
#     print(f'{aumento} % de aumento:      {preço + (preço*(aumento/100))}')
#     print(f'{diminuir} % de aumento:      {preço - (preço*(diminuir/100))}')
#     print('-='*45)
#     return print(f"""O preço analisado:    R$ {preço:<15.2f}\nO Dobro do preço:     R$ {preço*2:<15.2f}\nA metade do preço:    R$ {preço/2:<15.2f}\n{aumento} % de aumento:      R$ {preço + (preço*(aumento/100)):<15.2f}\n{diminuir} % de aumento:      R$ {preço - (preço*(diminuir/100)):<15.2f}""".replace('.', ','))
#
