#Minha Versão!

# def jogador(nome=" alberto", gols=0):
#     nome = input('Digite o nome do jogador: ')
#     gols = input('Digite o número de gols: ')
#     nome = nome.strip()
#     print('O jogador ', end="")
#     if nome == "":
#         print('<desconhecido>',end=" ")
#     else:
#         print(f"{nome}",end=" ")
#     if gols.isnumeric() == True:
#         print(f'fez {gols} gols.')
#     else:
#         print(f" fez 0 gols")
#         gols = 0
#
#
# jogador()


#Versão GUANABARA

def ficha(jog="<desconhecido>", gol=0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')


#Programa principal

n = str(input('Nome do Jogador: '))
g = str(input('Número de gols:'))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == "":
    ficha(gol=g)
else:
    ficha(n, g)

