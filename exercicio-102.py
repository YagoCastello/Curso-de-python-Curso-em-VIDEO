def fatorial(num, show=False):
    """
        :param num: VALOR DA FATORIAL
        :param show: DECIDIR SE MOSTRA OU NÃO TODOS OS TERMOS DA CONTA
        :return: NÃO TEM RETORNO
    """
    valor = 1
    for c in range(1, num+1):
        valor *= c
        if show:
            if c == num:
                print(f'{c} X ', end="")
            else:
                print(f'{c} X ', end="")
    print(f'= {valor}')


fatorial(6, True)
fatorial(num=int(input('Digite o valor da fatorial: ')))
