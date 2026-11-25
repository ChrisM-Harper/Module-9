# Christopher Monarrez M9P1

# Variables
total_extended_price = 0


# Calculation

# Defining compute_ext_price Function
def compute_ext_price(quantity, unitprice):
    ext_price = (quantity * unitprice)

    if ext_price > 10000:
        ext_price = (ext_price * .9)

    return ext_price


# While Loop
while True:
    quantity = int(input("Enter the Quantity (Enter 0 to quit): "))

    if quantity == 0:
        break

    # Unit Price
    unit_price = float(input("Enter Unit Price: "))

    # Calc.
    ext_price = compute_ext_price(quantity, unit_price)
    total_extended_price = total_extended_price + ext_price


    # Display 1
    print("Quantity", quantity)
    print("Unit Price: ", unit_price)
    print("Extended Price: ", ext_price)

# Display Extended Price Total
print()
print("Extended Price Total: ", total_extended_price)

