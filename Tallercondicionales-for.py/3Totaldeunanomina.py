"""
EJERCICIO 3
Una empresa tiene N empleados, con 0 <=N <= 1000
Se recibe el sueldo de cada empleado
y se desea el total de nomina
Para una empresa sin empleados,
El total es 0"""

N_empleados = int(input("Ingrese el numero de empleados: "))
nomina = 0

if N_empleados < 0 or N_empleados > 1000:
    print ("cantidad de empleados invalida")
else:
    for i in range (1, N_empleados +1 ):
        sueldo = int(input("Ingrese sueldo del empleado: "+str(i)+str(": ")))
        nomina = nomina + sueldo
        print ("Nomina: ", nomina)
        