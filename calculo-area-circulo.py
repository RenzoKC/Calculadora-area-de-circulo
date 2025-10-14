import math


# Paso 1: Solicitar al usuario que ingrese el radio del círculo

radio = float(input("Ingrese el radio del círculo: "))

# Paso 2: Calcular el radio del círculo utilizando área = π * radio^2

area = math.pi * (radio**2)

# Paso 3: Mostrar al usuarioel resultado obtenido (área calculada)

print("El área del círculo con radio", radio, "es:", area)