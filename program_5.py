#Programmer: Timothy Pickering
#Date: 2/4/2025
#Title: Dog Price Calc

def calculate_cost():
    # Prices for hot dogs and toppings
    hotDogPrice = 3.50
    chiliDogPrice = 4.50
    cheesePrice = 0.50
    peppersPrice = 0.75
    grilledOnionsPrice = 1.00
    taxRate = 0.07

    # Input hot dog type
    hotDogType = input("What kind of dog day is it? (Hot Dog or Chili Dog): ").lower()

    if hotDogType == 'hot dog':
        basePrice = hotDogPrice
    elif hotDogType == 'chili dog':
        basePrice = chiliDogPrice
    else:
        print("Invalid hot dog type entered.")
        return

    # Running total for toppings
    toppingsTotal = 0  #running total of toppings

    # Input optional toppings
    cheese = input(f"Would you like cheese ({cheesePrice:.2f})? (yes/no): ")# Input optional toppings
    if cheese == 'yes':
        toppingsTotal += cheesePrice

    peppers = input(f"Would you like peppers ({peppersPrice:.2f})? (yes/no): ")# Input optional toppings
    if peppers == 'yes':
        toppingsTotal += peppersPrice

    grilledOnions = input(f"Would you like grilled onions ({grilledOnionsPrice:.2f})? (yes/no): ")# Input optional toppings
    if grilledOnions == 'yes':
        toppingsTotal += grilledOnionsPrice

    # Calculate subtotal, tax, and total
    subtotal = basePrice + toppingsTotal
    tax = subtotal * taxRate
    totalCost = subtotal + tax

    # Display results
    print("Order Cost:")
    print(f"Base price for {hotDogType}: ${basePrice:.2f}")
    print(f"Toppings: ${toppingsTotal:.2f}")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Tax (7%): ${tax:.2f}")
    print(f"Total cost: ${totalCost:.2f}")

# Call the function
calculate_cost()
