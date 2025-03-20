casa = float(input("Qual o valor da casa que deseja financiar? \n"))
salario = float(input("E qual o seu salário atual? \n"))
tempo = int(input("E em quantos anos pretende pagar? \n"))

parcela = casa / tempo
mensal = parcela / 12
prestacao = salario * 0.3
correto = casa / prestacao
anos = correto / 12

if mensal > prestacao:
    print("O valor da prestação ultrapassa 30% do valor do seu salário. \n")
    print("{} anos não são suficientes.".format(tempo))
    print("Você precisaria de no mínimo {} anos para não ultrapassar 30% do valor de seu salário.".format(round(anos)))
elif prestacao >= mensal:
    print("Você pagará R$ {} durante {} anos no valor mensal de R$ {}.".format(casa, tempo, prestacao))
    print("Para pagar confortavelmente esse valor, seriam necessários no mínimo {} anos.".format(round(anos)))