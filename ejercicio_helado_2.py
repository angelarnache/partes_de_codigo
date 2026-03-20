print("─bienvenido a heladeria celeste─")
productos=["cono $3000","vaso $4000","banana split $9000"]

fijo=3000
fijo_2=4000
fijo_3=9000

pedidos=[]
cantidad=[]
totales=[]

condicion="falso"
while condicion == "falso":
    while condicion == "falso":
        for menu in range(len(productos)):
            print(f"─{productos[menu]}")
        operacion=input("que desea pedir el cliente\n").lower()
        if operacion == "cono":
            pedidos.append(operacion)
            break
        elif operacion == "vaso":
            pedidos.append(operacion)
            break
        elif operacion == "babanasplit" or operacion == "banana split":
            pedidos.append(operacion)
            break
        else:
            print("esa no es una opcion valida")
            continue

    while condicion =="falso":
        try:
            operacion_2 = int(input("cantidad del pedido: "))
            cantidad.append(operacion_2)
            break   
        except ValueError:
            print("opcion invalida intente de nuevo")
            continue

    if operacion == "cono":
        total = cantidad[0]*fijo
        guarda = total
        totales.append(guarda)
    elif operacion == "vaso":
        total_2 = cantidad[0]*fijo_2
        guarda_2 = total_2
        totales.append(guarda_2)
    elif operacion == "babanasplit" or operacion == "banana split":
        total_3 = cantidad[0]*fijo_3
        guarda_3= total_3
        totales.append(guarda_3)
    
    operacion_3=input("deseas registrar mas productos si/no:\n").lower()
    if operacion_3 == "si" or operacion_3 == "s":
        continue
    elif operacion_3 == "no" or operacion_3 == "n":
        break

conteo=len(pedidos)
print(f"se atendieron un total de: {conteo} clientes")
print(f"lista de productos vendidos {pedidos} \n{cantidad} \n{totales}")
sumatora =sum(totales)
print(f"la sumatoria total es de: {sumatora}")

mas_repetido = max(set(pedidos), key=pedidos.count)
frecuencia = pedidos.count(mas_repetido)
print(f"el producto mas repetido es {mas_repetido}:con frecuencia {frecuencia} ")
