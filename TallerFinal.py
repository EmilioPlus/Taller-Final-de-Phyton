#1) Escribir un algoritmo que calcule el producto escalar y
#vectorial de dos vectores de 3 elementos cuyos valores se
#introducen por pantalla.

Vect1 = 3*[0] 
Vect2 = [0]*3 
#Entradas
for i in range(3):
    Vect1[i] = int( input("V1({}): ".format(i+1)))
for i in range(3):
    Vect2[i] = int( input("V2({}): ".format(i+1)))
#Proceso
sum = 0
for i in range(3):
    Prod = Vect1[i]*Vect2[i]
sum = sum + Prod
print("El producto escalar es:", sum)
x = Vect1[1]* Vect2[2] - Vect1[2]* Vect2[1]
y = -( Vect1[0]* Vect2[2] - Vect1[2]* Vect2[0] )
z = Vect1[0]* Vect2[1] - Vect1[1]*Vect2[0]
print("El producto vectorial es: {}i {}j {}k".format(x, y, z))


#2) Escribir un algoritmo que pida un vector de caracteres por
#pantalla e invierta el orden de los caracteres mostrándolo por
#pantalla. La inversión se hará sin utilizar otro vector auxiliar.

print("Ingrese la dimensión del vector: ");
Nu = int( input())
vect = Nu*[''] 
for i in range(Nu):
    v[i] = input("Ingrese el Caracter: ")
#Proceso
z = ''
d = Nu
for i in range(Nu//2):
    z = vect[i]
vect[i] = vect[d-1]
vect[d-1] = z
d = d - 1
#Salida
for i in range(Nu):
    print(vect[i])


#3) Escribir un algoritmo que calcule los números primos de 0 a
#100 utilizando el llamado método de la criba de Eratóstenes. 

B = 100*[True]
N = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
    17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
    31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44,
    45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58,
    59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 
    73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84,85, 86, 
    87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
for i in range(1, 100+1):
    N.append(i)
#Proceso
B[0] = False
for i in range(1, 99):
    for j in range(i+1, 100):
        if N[j] % N[i] == 0:
            B[j] = False
for i in range(100):
#Si el valor de B[i] = 1
    if B[i]:
        print(N[i])


#4) Realizar un algoritmo que maneje un vector de enteros a través
#de un menú con seis opciones:

#Inicializar
V = 100*[0] #Inicializamos un vector con 100 elementos por defecto
i = 0
print ("Ingrese tamaño del vector")
n = int( input())
opc = -1
while opc != 0:
    print("\n")
    print("Ingrese 1 para añadir un elemento al vector")
    print("Ingrese 2 para eliminar un elemento del vector")
    print("Ingrese 3 para listar el contenido del vector ")
    print("Ingrese 4 para contar las apariciones de Un número en el vector")
    print("Ingrese 5 para calcular la media y el máximo de los elementos de un vector")
    print("Ingrese 0 para terminar")
#Leer Opcion
opc = int( input("Ingrese Opción: "))
if opc == 1:
    if (i < n) :
        #Agraga en la posicion 0 y luego incrementa i
        V[i] = int( input("IngreseEntero: "))
        i = i + 1
elif opc == 2:
    print("Ingrese el número que desea eliminar")
    num = int( input())
if num > 0:
    a = 0
    #Busca NUM en el array
    for j in range(i):
        if V[j] == num :
            a = j
            break
#Re-organizar el array
if a >= 0 and a <= i:
    for j in range(a, i-1 +1):
        V[j] = V[j+1]
    V[i] = 0
    i = i - 1
elif opc == 3:
    if i > 0:
        for j in range(i):
            print(V[j])
elif opc == 4:
    c = 0
    print("Ingrese numero para contar número de apariciones: ")
    num = int( input())
    for j in range(i):
        if num == V[j] :
            c = c + 1
    print(" El número de apariciones es: ", c)
elif opc == 5:
    max = V[0]
    ma = 0
    for j in range(i):
        if max < V[j]:
            max = V[j]
        ma = ma + V[j]
    ma = ma/i
    print("El maximo es:", max, " y la media es: ", ma)

elif opc == 0:
    print("FIN DE PROGRAMA")
    break

#5) Elaborar algoritmo que busque en forma secuencial un
#VALOR dentro de un arreglo de N elementos numéricos y
#retorne su posición. 

valor = []
print ("Ingrese la cantidad de elementos del arreglo")
m = int( input())
print ("Ingrese los elementos del arreglo")
for i in range(m) :
    elemento = int( input("Ingrese el Elemento numerico: "))
    valor.append(elemento)
#Búsqueda del valor dentro del arreglo
print ("Ingrese el valor que desa buscar: ")
bus = int( input())
for i in range(m) :
    if valor[i] == bus :
        r = i
        print ("La posición del elemento es", r+1)
        break

#6) Elaborar un algoritmo que ordene descendentemente un vector.

Vect1 = []
print ( "Ingrese cantidad de elementos del vector: ")
n = int( input())
print ( "Ingrese los valores del vector: ")
for x in range(n):
    valor = int( input("V{}: ".format(x+1)))
    Vect1.append(valor)
print ( "Los elementos del vector son: ")
for y in range(n):
    for x in range(n-1):
        if Vect1[x] < Vect1[x+1]:
            m = Vect1[x]
            Vect1[x] = Vect1[x+1]
            Vect1[x+1] = m
print(Vect1)

#7) Realizar un algoritmo que introduzca un nuevo elemento en
#un vector ordenado ascendentemente, el vector debe conservar
#el orden.

Vectr = []
print("Ingrese los 10 valores del vector: ")
for i in range(10):
    valor = int( input("valor {}: ".format(i+1)))
    Vectr.append(valor)
valor = int( input("Ingrese valor a insertar: "))
Vectr.append(valor)
#Ordenar el vector
for x in range(11):
    for y in range(10):
        if Vectr[y] > Vectr[x]:
            a = Vectr[y]
            Vectr[y] = Vectr[x]
            Vectr[x] = a
for x in range(11):
    print(Vectr[x])


#8) Cargar un vector de 100 posiciones con numero enteros, a
#partir de este crear 2 vectores; uno con los números pares y el
#otro con los numero impares, además decir de los vectores
#cual es más grande y el número de elementos en cada vector.

Vec = []
print ("Ingrese dimensión del vector: ")
TamVec = int( input())
pares = TamVec*[0]
impares = TamVec*[0]
print ( "Ingrese los", TamVec, "valores del vector")
for x in range(TamVec):
    elemento = int( input("Elemento {}: ".format(x+1)))
    Vec.append(elemento)
vtr = 0
i = 0
for x in range(TamVec):
    if Vec[x] % 2 == 0:
        pares[vtr] = Vec[x]
        vtr = vtr + 1
else:
    impares[i] = Vec[x]
    i = i + 1
print(pares[0:vtr]) 
print ( "El vector de pares tiene" , vtr, "elementos")
print(impares[0:i])
print ( "El vector de impares tiene", i, "elementos")

#9) Se tiene un vector, se pide ingresar 200 nombres de animales,
#luego se debe buscar el nombre de un animal que se ingrese por teclado...

animal = []
print ("Ingresar dimensión del array: ")
tamArray = int( input())
print ( "Ingrese los nombres de los animales:")

for x in range(tamArray):
    elemento = input( "Ingrese el Animal: {} ".format(x+1) )
    animal.append(elemento)

print ( "Ingrese el animal a buscar:")
nom = input()
print ( "El animal tiene como vecino a:")
print("----------------")
for x in range(tamArray):
    if animal[x] == nom:
        if x == 0:
#Como es Primero: No tiene vecino Izquierdo
            print(animal[x+1])
    elif x == tamArray-1:
#Como es Ultimo: No tiene vecino Derecho
        print(animal[x-1])
else:
    print(animal[x-1])
    print(animal[x+1])





