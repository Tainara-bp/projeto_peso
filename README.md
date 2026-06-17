# 📊 Calculadora de IMC em Python

Projeto simples desenvolvido em Python para calcular o Índice de Massa Corporal (IMC) e informar a classificação do usuário.

## 🚀 Funcionalidades

- Recebe o peso do usuário em quilogramas (kg)
- Recebe a altura do usuário em metros (m)
- Calcula o IMC automaticamente
- Exibe a classificação de acordo com o resultado

## 🧮 Fórmula Utilizada

IMC = Peso / (Altura × Altura)

## 📋 Classificação

| IMC | Classificação |
|------|--------------|
| Menor que 18,5 | Magreza |
| 18,5 a 24,9 | Peso normal |
| 25,0 a 29,9 | Sobrepeso |
| 30,0 a 34,9 | Obesidade Grau I |
| 35,0 a 39,9 | Obesidade Grau II |
| 40,0 ou mais | Obesidade Grau III (Mórbida) |

## 💻 Código

```python
# Calculadora de IMC

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
```

## ▶️ Como Executar

1. Instale o Python.
2. Baixe ou clone este repositório.
3. Execute o arquivo:

```bash
python imc.py
```

## 📌 Exemplo

Entrada:

```text
Digite seu peso (kg): 70
Digite sua altura (m): 1.75
```

Saída:

```text
Seu IMC é: 22.86
Classificação: Peso normal
```

## 👩‍💻 Autora

Tainara Botelho

Projeto desenvolvido para estudos de Python e GitHub.
