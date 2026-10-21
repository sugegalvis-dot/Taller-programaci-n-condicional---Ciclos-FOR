"""
Ejercicio 2:
Se conoce el primer termino A
La diferencia D y la cantidad N (de terminos de una progresión)
A y D son enteros entre -100 y 10, y N está entre 0 y 1000
Determine la suma de los N términos; si N es cero, el total es cero.
"""

A = int(input("Ingrese el primer término A:  "))
D = int(input("Ingrese la diferencia D: "))
N = int (input("Ingrese la cantidad N: "))


if -100 <=A <=100 and -100 <=D <=100 and 0 <= N <= 1000:
    termino = A
    Suma = 0
    for k in range (N):
        Suma = Suma + termino
        termino = termino + D
        print ("suma: ", Suma)
else: 
    print ("Valores invalidos")

Suma_formula = N * (2* A + (N -1)* D) //2
print ("Suma: ", Suma_formula)