"""
Ejercicio 6:
Se reciben los tiempos de N ciclistas, con 1 ≤ N ≤ 20, 
sobre una vuelta de 250 metros. Cada registro contiene 
identificador entero positivo único, minutos enteros no negativos,
segundos entre 0 y 59 y centésimas entre 0 y 99. 
Cada tiempo total es positivo. 
Informe la velocidad media de cada ciclista en kilómetros
por hora y el identificador del ganador. En
empate de tiempo gana el primero recibido.
"""

t_menor = 0

N = int(input("Ingrese el N de ciclistas: "))

if 1 <= N <= 20:
    for r in range(1,N+1):
        id = int(input("identificador ciclista "))
        mins= int(input("minutos ciclista "+str(id)+str(": ")))
        segs = int(input("segundos ciclista "+str(id)+str(": ")))
        cents = int(input("centesimas ciclista "+str(id)+str(": ")))

        if id > 0 and mins >= 0 and 0 <= segs <= 59 and 0 <= cents <= 99:
            t = 60 * mins + segs + cents / 100

            if t > 0:    
                v = 900/t
                print("ciclista ",id,": ",v,"km/h")

            if t_menor == 0 or t < t_menor:
                t_menor = t
                ganador = id


    print("Ganador:", ganador)