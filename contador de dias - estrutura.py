from datetime import date

x = input("Seja bem vindo, digite os dados abaixo\n")

y = input("data inicial\n")

dia_inicial = int(input("Dia: "))
mes_inicial = int(input("Mês: "))
ano_inicial = int(input("Ano: "))

z = input("data final\n")

dia_final = int(input("Dia: "))
mes_final = int(input("Mês: "))
ano_final = int(input("Ano: "))

data_inicial = date(ano_inicial, mes_inicial, dia_inicial)
data_final = date(ano_final, mes_final, dia_final)

diferenca = data_final - data_inicial
if diferenca.days == 1:
    print(f"{diferenca.days} dia.")
else:
    print(f"{diferenca.days} dias.")