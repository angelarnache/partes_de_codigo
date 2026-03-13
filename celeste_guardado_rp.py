products = []
amounts = []
costs = []

def register_products(quantity_in=10):

    condicion = "true"

    while condicion == "true":
        print("\nWelcome to Celeste's Store")
        print("Choose your option:")
        print("1. Product registration")
        print("2. Bye bye litle bitch")
        
        try:
            option = int(input("What is your choise?: "))
        except ValueError:
            print("Invalid option, please choose a valid number.")
            continue

        if option == 1:
            for i in range(quantity_in):
                print(f"\n──── product {i+1} ─────")
                word = input("Enter product: ")
                word_2 = int(input("Enter quantity: "))
                word_3 = float(input("Enter the product cost: "))
                
                products.append(word)
                amounts.append(word_2)
                costs.append(word_3)
                
                
                option_2 = input("Do you want to continue? yes/no: ").lower()
                
                if option_2 == "no":
                    print("\nProduct list:")
                    print(f"Products: {products}")
                    print(f"Amounts: {amounts}")
                    
                    total = [x * y for x, y in zip(costs, amounts)]
                    print(f"Total per product: {total}")
                    print(f"Grand Total: {sum(total)}")
                    break 
                
        elif option == 2:
            print("See you later!")
            condicion = "false"

register_products()
