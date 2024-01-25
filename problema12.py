nombre_archivo = input('Ingrese el nombre del archivo:  ')
archivo_nuevo = nombre_archivo.replace('.','/')
extension = nombre_archivo.lower().split('.')[-1]

if extension == 'txt' or extension == 'gif' or extension == 'jpg'  or  extension == 'jpeg' :
    print(archivo_nuevo)
elif extension == 'png' or extension == 'pdf' or extension == 'zip' :
    print(archivo_nuevo)
else:
    print('application/octet-stream.')