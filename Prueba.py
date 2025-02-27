def calcular_imc(peso, altura):
    return peso / (altura ** 2)

# Pedimos los datos al usuario
peso = float(input("Ingresa tu peso en kg: "))
altura = float(input("Ingresa tu altura en metros: "))

# Calculamos el IMC
imc = calcular_imc(peso, altura)

# Clasificación del IMC
if imc < 18.5:
    categoria = "Bajo peso"
elif 18.5 <= imc < 24.9:
    categoria = "Peso normal"
elif 25 <= imc < 29.9:
    categoria = "Sobrepeso"
else:
    categoria = "Obesidad"

# Mostramos el resultado
print(f"Tu IMC es: {imc:.2f}")
print("Categoría:", categoria)
