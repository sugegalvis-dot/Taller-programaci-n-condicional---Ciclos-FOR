"""
EJERCICIO 7:
Se reciben N empleados, con 1 <= N <= 40. Cada registro contiene,
En este orden, identificador entero positivo unico, edad
entera no negativa en años y años enteros de antiguedad 
entre 1 y 50. El sueldo ficticio es la suma de una base 
de 100 unidades monetarias,
el valor numerico de la edad y la suma de los enteros desde
1 hasta la antiguedad; toda esa suma se divide entre
los años de antiguedad. La edad y la suma de años se
consideran aportes numéricos en unidades monetarias, dentro de 
este modelo fictici.

Informe el sueldo de cada empleado, el total de la nomina
y los identificadores con mayor y menor sueldo. 
En empate conserve el primero recibido.
"""

N = int(input("Ingrese la cantidad de empleados: "))

if 1 <= N <= 40:
    nomina = 0

    for i in range(N):
        id = int(input("Ingrese el dentificador empleado: "))
        edad = int(input("Ingrese edad del empleado: "))
        antig = int(input("Ingrese años de antigüedad: "))

        if edad >= 0 and 1 <= antig <= 50:
            suma = (antig * (antig + 1)) / 2
            sueldo = (100 + edad + suma) / antig

            nomina = nomina + sueldo

            print("Empleado", id, ":", sueldo)

            if i == 0:
                mayor = sueldo
                menor = sueldo
                id_mayor = id
                id_menor = id

            elif sueldo > mayor:
                mayor = sueldo
                id_mayor = id

            if sueldo < menor:
                menor = sueldo
                id_menor = id

    print("Nómina:", nomina)
    print("Mayor: Empleado", id_mayor, ":", mayor)
    print("Menor: Empleado", id_menor, ":", menor)

else:
    print("Número de empleados no válido")
    