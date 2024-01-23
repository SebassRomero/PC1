consumo = float(input('¿Cuanto fue su consumo? '))
propina = float(input('¿Que porcentaje(%) de propina desea dejar al mesero? '))

cantidadPro = consumo * (propina / 100)
print(f"La proprina del {propina}% es S/{cantidadPro} ")