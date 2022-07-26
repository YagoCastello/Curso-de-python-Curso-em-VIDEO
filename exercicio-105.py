# def notas(num):
#     soma = 0
#     num=int(*num)
#     maior =  menor=média=0
#     situação = ""
#     soma += num
#     dic={"Total" : soma }
#
#
#     print(f'soma {dic["Total"]}')
#
#
#
# #PROGRAMA PRINCIPAL
# resp = notas(5.5,8)
# print(resp)

#PROGRAMA PRINCIPAL

def notas(*n, sit=False):
    """
    ->Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'BOA'
        elif r['média'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r


#PROGRAMA PRINCIPAL
resp = notas(5.5, 7.5, 8, sit=True)
print(resp)
#help(notas)
