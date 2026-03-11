status = "si"

while status == "si":
    data = input("Ingrese un nombre: ")
    print (data)
    status = input("para continuar escriba si de lo contrarion escriba no: ")
______________________________________________
names=["angel","pedro","jose","maria","pedro","jorgee"]

def saludar(names):
    mensaje=f"hola {names}"
    mensaje2="adios"
    return mensaje,mensaje2
_______________________________________
for name in names:
    saludo=saludar(name)
    print(f"{saludo[0]} {saludo[1]}")
__________________________________________________
    LIST = []
for i in range(3):
    palabra = input("enter a word: ")
    LIST.append(palabra)
print(LIST)
