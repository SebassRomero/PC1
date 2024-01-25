hora_ingresada = input("Ingresa la hora en formato de 24 horas : ")
hora_ingresada_decimal = float(hora_ingresada.replace(':', '.'))

desayuno_inicio = 7.0
desayuno_fin = 8.0
almuerzo_inicio = 12.0
almuerzo_fin = 13.0
cena_inicio = 18.0
cena_fin = 19.0
        

if desayuno_inicio <= hora_ingresada_decimal <= desayuno_fin:
    print("Es hora de desayunar.")
elif almuerzo_inicio <= hora_ingresada_decimal <= almuerzo_fin:
    print("Es hora de almorzar.")
elif cena_inicio <= hora_ingresada_decimal <= cena_fin:
    print("Es hora de cenar.")
else:
    print("-----")