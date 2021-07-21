 # Mensagem de boas-vindas
print("Bem vindo(a) ao calculador de gorjetas!!!")

 # Cliente deverá digital o valor total da conta 
total = input("Qual foi o total da conta?\n " + "R$ ")

 # Cliente deverá escolher o valor da gorjeta

gorjeta = input("Qual porcentagem você gostaria de dar? 10%, 12%, ou 15%?\n")
 
 # Número de pessoas que irão dividir a conta

pessoas = input("Quantas pessoas irão dividir a conta?\n ")

 # Cálculo da conta multiplicando o valor pela porcentagem e depois divindo por cem

conta_final = float(total) * int(gorjeta) / 100

 # Resultado do valor referente a porcentagem + o valor total e divido pelo número de pessoas 

resultado = (float(conta_final) + float(total)) / int(pessoas)

 # Valor final da conta arredondada em duas casas decimais
conta_final_arredondada = round(resultado, 2)

 # Mensagem final informando o valor a ser pago por cada um

print(f"Cada pessoa deverá pagar: R$ {conta_final_arredondada} ")