# Hernadez Dylan NC 1245 
# Práctica 7 - Estructuras de Machine Learning
# p7-extructuras-1245.py


print("======================================")
print("PRACTICA 7 - ESTRUCTURAS DE ML")
print("Hernadez Dylan NC 1245  ")
print("======================================")


# ======================================
# 1. CONDICIONES
# ======================================


print("\n--- 1. CONDICIONES ---")


print("\nEjemplo 1:")
edad = 20
if edad >= 18:
    print("Es mayor de edad")


print("\nEjemplo 2:")
numero = 10
if numero > 5:
    print("El número es mayor que 5")




# ======================================
# 2. IF - ELIF
# ======================================


print("\n--- 2. IF - ELIF ---")


print("\nEjemplo 1:")
calificacion = 85


if calificacion >= 90:
    print("Excelente")
elif calificacion >= 70:
    print("Aprobado")
else:
    print("Reprobado")


print("\nEjemplo 2:")
edad = 20


if edad >= 60:
    print("Adulto mayor")
elif edad >= 18:
    print("Adulto")
else:
    print("Menor de edad")




# ======================================
# 3. IF - ELSE
# ======================================


print("\n--- 3. IF - ELSE ---")


print("\nEjemplo 1:")
edad = 18


if edad >= 18:
    print("Puede votar")
else:
    print("No puede votar")


print("\nEjemplo 2:")
numero = 7


if numero % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")




# ======================================
# 4. CICLO FOR
# ======================================


print("\n--- 4. CICLO FOR ---")


print("\nEjemplo 1:")
for numero in range(1, 6):
    print("Número:", numero)


print("\nEjemplo 2:")
for nombre in ["Adrian", "Luis", "Carlos"]:
    print("Nombre:", nombre)




# ======================================
# 5. CICLO WHILE
# ======================================


print("\n--- 5. CICLO WHILE ---")


print("\nEjemplo 1:")
contador = 1


while contador <= 5:
    print("Contador:", contador)
    contador += 1


print("\nEjemplo 2:")
numero = 5


while numero >= 1:
    print("Número:", numero)
    numero -= 1




# ======================================
# FIN
# ======================================


print("\n======================================")
print("FIN DE LA PRACTICA")
print("======================================")
print("Programa realizado por Hernadez Dylan NC 1245 ")