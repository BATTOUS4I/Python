
altura = float(input("Digite a sua altura: "))
peso = float(input("Digite o seu peso em kg: "))

imc = round(peso / (altura **2))

print(round(imc, 1))

if imc < 18.5:
  print(f"Seu IMC é {imc}, você está abaixo do peso.")
elif imc < 25:
  print(f"Seu IMC é {imc}, você tem um peso normal.")
elif imc < 30:
  print(f"Seu IMC é {imc}, você está um pouco acima do peso.")
elif imc < 35:
  print(f"Seu IMC é {imc}, você está obeso.")
else:
  print(f"Seu IMC é {imc}, você está clinicamente obeso."
)






