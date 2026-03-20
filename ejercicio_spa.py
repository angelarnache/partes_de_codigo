print("─bienvenido al spa celeste─")
lista=["masaje","facial","manicure"]

for menu in range(len(lista)):
    print(f"─{lista[menu]}")

condicion = "falso"
while condicion == "falso":
    operacion = input("que desea agendar: ").lower()
    if operacion == "masaje":
        print("se agendo un masaje")
        break
    elif operacion == "facial":
        print("se agendo un masaje facial")
        break
    elif operacion == "manicure":
        print("se agendo una manicure")
        break
    else:
        print("esa opcion no existe intente de nuevo")
        continue
