def register_products(quantity_in=1):
    products =[]
    amounts=[]
    costs=[]
    for i in range(quantity_in):
        print(f"\n────product {i+1}─────")
        word=input("Enter product: ")
        word_2=int(input("Enter quantity: "))
        word_3=float(input("Enter the product cost: "))
        products.append(word)
        amounts.append(word_2)
        costs.append(word_3)
    
        total = [ x * y for x, y in zip(costs, amounts)]
    print(total)
    return total
resultado="yes"

while resultado == "yes":
    resultado = input("Do you want to add more products?: ")
    if resultado =="yes":
        register_products()
    else:
        print("gracias")
        break

