num_shows = int(input("Ingrese cuántos shows musicales ha visto en el último año: "))

if num_shows > 3:
    visto = True
else:
    visto = False

print("¿Ha visto más de 3 shows musicales en el último año? : " + str(visto))
