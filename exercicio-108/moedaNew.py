def dobro(n):
    return f'R$ {n*2:.2f} '.replace('.', ',')


def moeda(n):
    return f'R$ {n:.2f} '.replace('.', ',')





def metade(n):
    return f'R$ {n/2:.2f} '.replace('.', ',')


def aumento(n, porcentagem):
    return f'R$ {n*(1+porcentagem/100):.2f} '.replace('.', ',')


def diminuir(n, porcentagem):
    return f'R$ {n*(1-porcentagem/100):.2f} '.replace('.', ',')


