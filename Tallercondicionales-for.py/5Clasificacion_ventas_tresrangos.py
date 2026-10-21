"""
Ejemplo 5:
Un vendedor tiene N ventas, con 0 ≤ N ≤ 1000, 
y se recibe el importe no negativo de cada una. 
Informe cuántas fueron de 200 o menos, cuántas superaron 200 sin llegar a 400 y cuántas
fueron de 400 o más. Una venta pertenece a un solo grupo
"""

N= int(input("Ingrese la cantidad de ventas: "))
importes = 0
grupo1 = 0
grupo2 = 0
grupo3 = 0

if N <= 0 or N >= 1000:
    print("Cantidad de ventas invalida")

else:
    for i in range(1, N+1):
        importes= int(input("Ingrese el valor de la venta "+str(i)+str(": " )))
        if importes <= 200:
            grupo1= (grupo1+1)
        elif importes > 200 and importes < 400:
            grupo2= (grupo2+1)
        elif importes >= 400:
            grupo3= (grupo3+1)

    print("Grupos 1,2 y 3:", grupo1, grupo2, grupo3)
    