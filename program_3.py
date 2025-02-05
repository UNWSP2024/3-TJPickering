#Programmer: Timothy Pickering
#Date: 2/4/2025
#Title: Shipping cost calc

def weight_conversion(weight): #categorizing ship cost by weight
    if weight <= 2:
        shippingCost = 1.50
    elif 2 < weight <=6:
        shippingCost = 3.00
    elif 6 < weight <=10:
        shippingCost = 4.00
    else 10 < weight :
        shippingCost = 4.75
    return shippingCost
#-----------------------------------------------------------------
if __name__ == '__main__':
    # Local variables
    weight = 0.0
    shippingCost = 0.0
    # Get package weight from the user.
    weight = float(input('Enter the weight of the package: '))
    # Display the shipping charge.
    shippingCost = weight_conversion(weight)
    print ('Shipping charge: $', format(shippingCost, '.2f'))
