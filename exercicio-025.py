x=str(input('Qual é o seu nome completo?')).strip()
print('{}Seu nome tem Silva?  {}{}'.format('\033[4;32;46m','SILVA' in x.upper(),'\033[m'))
