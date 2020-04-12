#1. Se requiere un algoritmo para obtener la edad promedio de un grupo de N alumnos. Si algún alumno tiene más de 18 años, se muestra el promedio que se lleva sin contar el alumno de 18 años. EL usuario decide si desea cerrar el programa o vuelve a ejecutarlo.

validacion = True

while validacion == True:
    num_alumnos = 0
    edad_alumno = 0
    edad_promedio = 0
    c_edad = 0
    a_edad = 0
    num_alumnos = input("Ingrese el número de alumnos: ")
    for i in range(int(num_alumnos)): 
        edad_alumno = input("Ingrese la edad de un alumno: ")
        if int(edad_alumno) >= 18: 
            print("la ultima edad ingresa es mayor o igual a 18 años")
            break
        c_edad = c_edad+1
        a_edad = a_edad + int(edad_alumno)
        

    edad_promedio = a_edad / c_edad
    print("Edad Promedio: " + str(edad_promedio))
    
    respuesta = input("Desea realizar otro promedio: si/no  ")
    if respuesta.lower() == "no":
        validacion = False


#2. Se requiere un algoritmo para obtener la suma de diez cantidades mediante la utilización de un ciclo for.

suma = 0
for i in range(10):
    cantidad = input("Ingrese la cantidad que desea sumar: ")
    suma = suma + int(cantidad)
print("La suma de los valores es: " + str(suma))


#3. Se requiere un algoritmo para obtener la estatura promedio de un grupo de personas, cuyo número de miembros se desconoce, el ciclo debe efectuarse siempre y cuando se tenga una estatura registrada.
#salir del while cuando sea string o este vacio
a_estatura = 0
c_estatura = 0
estatura = 0
validacion = True

while int(len(str(estatura))) != 0 and validacion == True:
    estatura = input("digite una estatura (cms): ")
    if estatura.isnumeric():
        estatura = int(estatura)
        a_estatura = a_estatura + estatura
        c_estatura = c_estatura + 1
    else:
        validacion = False


#4. Se requiere un algoritmo para determinar, de N cantidades, cuántas son menores o iguales a cero y cuántas mayores a cero.
num_cantidades = int(input("Cuantas cantidades se van a ingresar: "))
c_mayor = 0
c_menor = 0

for i in range(num_cantidades):
    cantidad = int(input("Ingrese la cantidad: "))
    if cantidad > 0:
        c_mayor = c_mayor + 1
    elif cantidad <= 0:
        c_menor = c_menor + 1

print("Cantidades mayores a 0 (cero): " + str(c_mayor))
print("Cantidades menores o iguales a 0 (cero): " + str(c_menor))


#5. Realice un algoritmo para generar e imprimir los números pares e impares que se encuentran entre 0 y 100. Además muestre la multiplicación de todos estos.

for i in range(10):
    print(i)


pares = []
impares = []
par = 1
impar = 1

for i in range(100):
    i=i+1
    if (i % 2) == 0:
        
        par = par * i
        pares.append(i)
    else:
        
        impar = impar * i
        impares.append(i)

print("Números pares: ")
print(pares)
print("Números impares: ")
print(impares)
print("Multiplicacion de los pares: " + str(par))
print("Multiplicacion de los impares: " + str(impar))


#6. Realice un algoritmo para generar N elementos de la sucesión de Fibonacci (0, 1, 1, 2, 3, 5, 8, 13,…).
a = 0
b = 1
n = 0
serie = 0
n = input("Digite el número de elementos al q se le desea aplicar la serie Fibonacci")
n = int(n)

print(str(a) + ", ")
for i in range(n - 1):
    print( str(b) + ", ")
    serie = a+b
    a = b
    b = serie

