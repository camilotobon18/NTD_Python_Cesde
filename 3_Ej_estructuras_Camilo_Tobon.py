
#Materia de mejor nota y promedio del alumno
calificaciones = {"calculo": 4, "dibujo": 5, "programacion": 4.5}

nota_mayor = 0
a_notas = 0
c_notas = 0
for x in calificaciones:
    if calificaciones[x] > nota_mayor:
        nota_mayor = calificaciones[x]
        materia_nota_mayor = x
    a_notas = a_notas + calificaciones[x]
    c_notas = c_notas + 1

promedio = a_notas / c_notas
print("El promedio del alumno es: " + str(promedio))
print("La materia de mejor nota es: " + str(materia_nota_mayor))

#Listado de numeros.
listado = []
for i in range(10):
    valor = int(input("Por favor ingrese un numero: "))
    listado.append(valor)

a_numeros = 0
c_numeros = 0

for x in listado:
    a_numeros = a_numeros + x
    c_numeros = c_numeros + 1 

num_mayor = max(listado)
num_menor = min(listado)
media = a_numeros / c_numeros

print("La sumatoria de todos los números es " + str(a_numeros))
print("El promedio es " + str(media))
print("El número mayor es " + str(num_mayor))
print("El número menor es " + str(num_menor))

#Palindromo

frase = input("Digita una frase:\n")

frase_inversa = ""
lista = []
for i in frase:
    lista.insert(0, i)

frase_inversa = "".join(lista)

if frase == frase_inversa:
    mensaje = "Es un palindromo"
else:
    mensaje = "No es un palindromo"

print(mensaje)

alfabeto = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10, 'k':11, 'l':12, 'm':13, 'n':14, 'ñ':15, 'o':16, 'p':17, 'q':18, 'r':19, 's':20, 't':21, 'u':22, 'v':23, 'x':24, 'y':25, 'z':26}
texto = input("Por favor digite una palabra o frase: \n")
texto = texto.lower()

numero = ""
for i in texto:
    for x in alfabeto:
        if i == x:
            numero = numero + str(alfabeto[x]) + "-"

print(numero)


#Vocales
vocales = ["a", "e", "i", "o", "u"]

oracion = input("Digite una oración: \n")

c_vocales = 0
for j in oracion:
    for k in vocales:
        if j == k:
            c_vocales = c_vocales + 1

print("La cantidad de vocales en la frase es " + str(c_vocales))


#conteo por cada una de las vocales
arreglo_vocales = ([["a", 0], ["e", 0], ["i", 0], ["o", 0], ["u", 0]])
print(arreglo_vocales)
frase_usuario = input("Escriba una oración\n")

for i in frase_usuario:
    for j in range(len(arreglo_vocales)):
        if arreglo_vocales[j][0] == i:
            arreglo_vocales[j][1] = arreglo_vocales[j][1] + 1

for i in range(len(arreglo_vocales)):
    print(str(arreglo_vocales[i][0]) + " = " + str(arreglo_vocales[i][1]))

#Eliminar las vocales de un string
frase_ingresada = input("Por favor ingrese una frase: \n")

nuevo_string = ""
for i in frase_ingresada:
    nuevo_string = nuevo_string + i
    for j in vocales:
        if i == j:
            nuevo_string = nuevo_string.replace(i, "")
print(nuevo_string)

#Números pares del 0 al 100
for i in range(0, 100 + 1):
    if i % 2 == 0:
        print(i)

#Palabra que mas se repite en el 1er parrafo de Frankenstein
parrafo = "Una desapacible noche de noviembre contemplé el final de mis esfuerzos. Con una ansiedad rayana en la agonía, coloqué a mí alrededor los instrumentos que me iban a permitir infundir un hálito de vida a la cosa inerte que yacía a mis pies. Era ya la una de la madrugada; la lluvia golpeaba las ventanas sombríamente, y la vela casi se había consumido, cuando, a la mortecina luz de la llama, vi cómo la criatura abría sus ojos amarillentos y apagados. Respiró profundamente y un movimiento convulsivo sacudió su cuerpo."
parrafo = parrafo.replace(",", "")
parrafo = parrafo.replace(".", "")
parrafo = parrafo.replace(":", "")
parrafo = parrafo.replace(";", "")
listado_palabras = parrafo.split()
conteo_palabras = list(set(listado_palabras))

mayor_conteo = 0
for indice, palabra in enumerate(conteo_palabras):
    conteo = listado_palabras.count(palabra)
    if mayor_conteo < conteo:
        mayor_palabra = palabra
        mayor_conteo = conteo

print("La palabra que mas se repite es: " + mayor_palabra + " con " + str(mayor_conteo) + " repeticiones.")



