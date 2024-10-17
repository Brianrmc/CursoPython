#Comicion de los vendedores

#Varaibles donde se guardar la informacion que se solicita
nombre = input("por favor escribe tu nombre: ")
ventas = input("Diga sus ventas totales del mes: ")

ventas = int(ventas)
comision = ventas* 13 / 100

comision = round(comision),2

print(f"Hola {nombre}, tus comisiones de este mes son de ${comision}")


