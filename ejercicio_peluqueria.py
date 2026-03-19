print("─peluqueria celeste─")


condicion="falso"
while condicion == "falso":
    opcion = input ("por favor digite la hora de llegada: ")
    if opcion.isdigit():
        opcion=int(opcion)
        break
    else:
        print("opcion invalida intenta de nuevo")
        continue

if opcion < 6:
    print("lo sentimos no estamos disponibles")
elif opcion >= 6 and opcion <=11:
    print("hora de mañana estamos disponibles")
elif opcion >= 12 and opcion <=17:
    print("hora de tarde estamos disponibles")
elif opcion >= 18 and opcion <=22:
    print("hora de noche estamos disponibles")
elif opcion >= 23:
    print("lo sentimos no estamos disponibles")
