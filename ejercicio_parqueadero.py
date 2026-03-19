print("--Parqueadero Celeste--")
print("--hora $5000--")
print("--por cada hora extra son $3000--")
fijo =5000
fijo_2 = 3000

condicion="falso"
while condicion == "falso":
    opcion = input ("cuantas horas vas a estar: ")
    if opcion.isdigit():
        opcion=int(opcion)
        break
    else:
        print("opcion invalida intenta de nuevo")
        continue

if opcion == 1:
    print("la hora a pagar es de $5000")
elif opcion >= 2:
    horas_e=[]
    horas_e.append(opcion)
    total = horas_e[0]*fijo_2
    total_2= total+fijo
    print(f"las horas a pagar ${total_2}")
