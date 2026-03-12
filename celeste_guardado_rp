def register_products(quantity_in=1):
    product =[]
    amount=[]
    cost=[]
    for i in range(quantity_in):
        print(f"\n────product {i+1}─────")
        word=input("Enter product: ")
        word_2=int(input("Enter quantity: "))
        word_3=float(input("Enter the product cost: "))
        product.append(word)
        amount.append(word_2)
        cost.append(word_3)
    
        
        resultado="yes"
        while resultado == "yes":
            resultado = input("Do you want to add more products?: ")
        if resultado =="yes":
            return register_products()
        else:
            print("gracias")
            break
    return product,amount,cost

a=register_products
print("listo")
print(a)
