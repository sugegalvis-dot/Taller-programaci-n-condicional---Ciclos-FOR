"""
Ejercicio 4:
Una inversión ficticia inicia con capital C no negativo 
y mantiene una tasa anual porcentual I con 0 < I < 100.
e recibe tamién un entero M entre 0 y 50. EL 
interes de cada añ. Determine el saldo despues de M años; M = 0 conserva el capital inicial
"""

C = int(input("Ingrese capital inicial: "))
I = int(input("Ingrese la tasa anual porcentual: "))
M = int(input("Ingrese la cantidad de años: "))

saldo_nuevo = C

if M == 0:
    saldo_nuevo= 0
elif 0 < I < 100:
    for k in range (M):
        saldo_nuevo = saldo_nuevo * (1 + I /100)
    print (saldo_nuevo)
