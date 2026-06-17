# Calculadora de IMC
import os
os.system("cls")

peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

imc = peso / (altura ** 2)

print(f"\nSeu IMC é: {imc:.2f}")

if imc < 18.5:
    print("Classificação: Magreza")
elif imc < 25:
    print("Classificação: Peso normal")
elif imc < 30:
    print("Classificação: Sobrepeso")
elif imc < 35:
    print("Classificação: Obesidade Grau I")
elif imc < 40:
    print("Classificação: Obesidade Grau II")
else:
    print("Classificação: Obesidade Grau III (Mórbida)")