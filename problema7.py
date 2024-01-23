numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))
print('\n')
print("Seleccione una opción:")
print("Presione 1. Mostrar la suma de los dos números")
print("Presione 2. Mostrar la resta (primer número - segundo número)")
print("Presione 3. Mostrar la multiplicación de los dos números\n")

opcion = int(input("Ingrese el número de la opción deseada : "))

if opcion == 1: 
   print( f"La suma es : {numero1 + numero2}") 
elif opcion == 2: 
   print( f"La resta es : {numero1 - numero2}")
elif opcion == 3: 
   print( f"La multiplicación es : {numero1 * numero2}")   
else: 
   print('No es correcto , ingrese los números establecidos')