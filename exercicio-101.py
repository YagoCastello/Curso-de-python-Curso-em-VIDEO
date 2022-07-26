
def voto(ano):
    import datetime
    idade = datetime.date.today().year - ano
    if idade >= 65:
        return f'{idade} anos, Voto OPCIONAL!'
    elif 16 <= idade < 65:
        return f'{idade} anos, Voto OBRIGATÓRIO!'
    else:
        return f'{idade} anos, Voto NEGADO!'


# PROGRAMA PRINCIPAL
print(voto(1940))
print(voto(2010))
print(voto(2003))
x = voto(2003)
y = voto(1956)
z = voto(2021)
print(f'O candidato x pode votar? {x} O candidato y pode votar? {y} O candidato x pode votar? {z}')

vc = int(input('Digite o seu ano de nascimento: '))
print(voto(vc))