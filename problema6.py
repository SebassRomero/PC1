edad = int(input('Ingrese edad: '))

if edad < 4 :
    print('Puede entrar gratis')
if edad >= 4 and edad < 18 :
    print('Debe pagar $5')
elif edad >=18 :
    print('Debe pagar $10')