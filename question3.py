cart = {}

while True:
    print("\nMenu:")
    print("1. Add item to cart")
    print("2. Remove item from cart")
    print("3. Calculate total price")

    choice = input("Enter your choice (1-3): ")

    if choice == '1':
        while True:
            item = input("Enter item name: ")
            item_price = float(input(f"Enter price for {item}: "))
            cart[item] = item_price
            more_items = input("Do you want to add another item? (y/n): ").lower()
            if more_items != 'y':
                break
    elif choice == '2':
        item = input("Enter item name that you want to remove: ")
        if item in cart:
            remove_item= cart.pop(item)
            print(f"{item} removed from cart.")
        else:
            print(f"{item} is not in your cart.")

    elif choice == '3':
        if cart:
            print("\nTotal Price:")
            total = 0
            for item, price in cart.items():
                print(f"{item}: Ksh {price}")
                total += price

            if total > 100:
                discount = total * 0.10
                total = total-discount
            print(f"Total amount to pay: Ksh {total}")
        else:
            print("Your cart is empty.")
        break

    else:
        print("Invalid choice! Please enter 1-3.")
