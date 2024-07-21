import gzip

input = open("C:/Users/ASUS/Desktop/SISS/Proyectos/Tarea Ejecutar proceso/Reporte Cliente.txt",'rb')
s=input.read()
input.close()

output = gzip.GzipFile("C:/Users/ASUS/Desktop/SISS/Proyectos/Tarea Ejecutar proceso/Comprimido/Reporte Cliente.txt.gz",'wb')
output.write(s)
output.close()

print("Done")