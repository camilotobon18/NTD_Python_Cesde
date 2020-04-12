import math
import datetime
from datetime import timedelta
#Area triangulo
def area_triangulo(b, h):
    area = (b * h) / 2
    return area

base = float(input("Por favor digite la base del triangulo: "))
altura = float(input("Por favor digite la altura del triangulo: "))

resultado = area_triangulo(base, altura)
print("El área del triangulo es: " + str(resultado))

#Dolares a pesos
def conversion(usd, tc):
    resultado = usd * tc
    return resultado

dolares = float(input("Por favor ingrese la cantidad de dolares a convertir: \n"))
tasa_cambio = float(input("Por favor ingrese la tasa de cambio: \n"))
usd_cop = conversion(dolares, tasa_cambio)
print("Los dolares ingresados equivalen a COP " + str(usd_cop))


#Celsius a Fahrenheit
def celsius_a_fahrenheit(grados):
    resultado = (grados * 9 / 5) + 32
    return resultado

celsius = float(input("Por favor ingrese los grados Celsius (Centigrados) a convertir:\n"))
result = celsius_a_fahrenheit(celsius)

print("Los grados Celsius ingresados corresponden a " + str(result) + " grados Fahrenheit")


#Cantidad de segundos que tiene un lustro (5 años)
def lustro_a_segundo():
    lustro = 5
    segundos = lustro * 365 * 24 * 60 * 60
    return segundos

segundos = lustro_a_segundo()
print("La cantidad de segundos que tiene un lustro (periodo de 5 años) es: " + str(segundos) + " segundos")


#Cantidad de segundos que le toma a la luz viajar del sol a marte
def sol_a_marte():
    #km
    distancia = 227940000
    #km/s
    velocidad = 300000
    resultado = distancia / velocidad
    return resultado


viaje = sol_a_marte()
print("La cantidad de segundos que le toma a la luz en viajar del sol a marte es: " + str(viaje) + " segundos")


#Vueltas de una llanta en 1Km, diametro de la llanta es 50cm
def vueltas():
    #conversion de las medidas a metros
    diametro = 50 / 100
    distancia = 1 * 1000
    pi = math.pi
    longitud = distancia / (diametro * pi)
    return longitud

nro_vueltas = vueltas()
print("El numero de vueltas que da una llanta de 50cm de diametro al recorrer un 1Km es: " + str(nro_vueltas))


#Longitud de la sombra de un edificio
def longitud_sombra(altura, angulo):
    sombra = altura / math.tan(angulo)
    return sombra

altura = 20
angulo = 22
sombra = longitud_sombra(altura, angulo)
print("De un edificio de 20 metros de altura cuando el ángulo que forman los rayos del sol con el suelo es de 22°. La sombra es de: " + str(sombra) + "mts")


#Comparación de edades
def compara_edades(edad1, edad2):
    if edad1 == edad2:
        mensaje = True 
    else:
        mensaje = False
    return mensaje 

edad1 = int(input("Digite la edad de la primer persona: "))
edad2 = int(input("Digite la edad de la segunda persona: "))

resultado_edad = compara_edades(edad1, edad2)
print("Al comparar ambas edades, el resultado fue: " + str(resultado_edad))


#Promedio de un alumno
materias = ["Español", "Matemáticas", "Economía", "Programación", "Ingles"]
a_notas = 0
c_notas = 0

for i in range(len(materias)):
    nota = float(input("Digite la nota para la materia: " + materias[i-1] + ": "))
    a_notas = a_notas + nota
    c_notas = c_notas + 1

promedio = a_notas / c_notas
print("El promedio de las 5 materias es: " + str(promedio))
