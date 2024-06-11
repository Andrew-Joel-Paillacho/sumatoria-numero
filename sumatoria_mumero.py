

numero = int(input("____________________\nPor favor, ingresa un número entero: "))

print("____________________\nElige una opción:")
print("1. Sumar todos los números desde los negativos hasta los positivos del número.")
print("2. Dividir el número en dos partes y sumar cada parte por separado.")

opcion = input("Ingresa el número de la opción que deseas (1 o 2): ")

print("____________________\n")  
if opcion == "1":
    suma_negativos = sum(range(-numero, 0)) 
    suma_positivos = sum(range(1, numero + 1)) 
        
    print(f"Números negativos desde {-numero} hasta -1: {list(range(-numero, 0))}")
    print(f"Números positivos desde 1 hasta {numero}: {list(range(1, numero + 1))}")
    print("____________________\n")
    print(f"La suma de los números negativos es: {suma_negativos}")
    print(f"El cero: 0")
    print(f"La suma de los números positivos es: {suma_positivos}")
    
elif opcion == "2":
    mitad = numero // 2
    if numero % 2 == 0:
        suma_izquierda = sum(range(1, mitad + 1))
        suma_derecha = sum(range(mitad + 1, numero + 1))
        print(f"Números de la izquierda: {list(range(1, mitad + 1))}")
        print(f"Números de la derecha: {list(range(mitad + 1, numero + 1))}")
        print("____________________\n")
        print(f"La suma de la primera mitad ({1} a {mitad}) es: {suma_izquierda}")
        print(f"La suma de la segunda mitad ({mitad + 1} a {numero}) es: {suma_derecha}")
    
    else:
        suma_izquierda = sum(range(1, mitad + 1))
        suma_derecha = sum(range(mitad + 2, numero + 1))
        print(f"Números de la izquierda: {list(range(1, mitad + 1))}")
        print(f"Números de la derecha: {list(range(mitad + 2, numero + 1))}")
        print("____________________\n")
        print(f"La suma de la primera mitad ({1} a {mitad}) es: {suma_izquierda}")
        print(f"Número central: {mitad + 1}")
        print(f"La suma de la segunda mitad ({mitad + 2} a {numero}) es: {suma_derecha}")
    
else:
    print("Opción no válida. Por favor, elige 1 o 2.")

print("____________________\n")

