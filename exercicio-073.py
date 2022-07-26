times=("Flamengo","Santos","Palmeiras","Grêmio-RS",
       "Athletico Paranaense-PR","São Paulo-SP",
       "Internacional-RS","Corinthians-SP","Fortaleza-CE",
       "Goiás-GO","Bahia-BA","Vasco da Gama-RJ","Athlético-MG",
       "Fluminense-RJ","Botafogo-RJ","Ceará-CE","Cruzeiro-MG","Csa-AL","Chapecoense-SC","Avaí-SC")
print("{:_^40}".format("Brasileirão 2019"))
opcoes=int(input("Escolha uma das opções abaixos:\n[1] Todos os times e suas colocações. \n[2] Os cincos primeiros colocados. \n[3] Os últimos quatro colocados. \n[4] Os todos os times, em ordem alfabética. \n[5] A posição da Chapecoense-SC\n[6] Todas as opções. \nDigite a sua opção:"))
if opcoes==1:
    for c in range(0,20):
        print("{} em {}º".format(times[c],c+1))
elif opcoes==2:
    for c in range(0,5):
        print("{} em {}º".format(times[c],c+1))
elif opcoes == 3:
    for c in range(16,20):
        print("{} em {}º".format(times[c],c+1))
elif opcoes ==4:
    print(" {}".format(sorted(times)))
elif opcoes==5:
    print(f'A Chapecoense-SC está na {(times.index("Chapecoense-SC")+1)}º')
elif opcoes==6:
    print("[1] Todos os times e suas colocações.")
    for c in range(0,20):
        print("{} em {}º".format(times[c],c+1))
    print("[2] Os cincos primeiros colocados.")
    for c in range(0,5):
        print("{} em {}º".format(times[c],c+1))
    print("[3] Os últimos quatro colocados.")
    for c in range(16,20):
        print("{} em {}º".format(times[c],c+1))
    print("[4] Os todos os times, em ordem alfabética.")
    print("{}".format(sorted(times)))
    print("[5] A posição da Chapecoense-SC")
    print(f'A Chapecoense-SC está na {(times.index("Chapecoense-SC") + 1)}º')

