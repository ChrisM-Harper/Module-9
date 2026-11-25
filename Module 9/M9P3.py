# Christopher Monarrez M9P3

# Variables
number_of_trips = 0


# Calculations

# Defining MPG Function
def mpg_function(miles, gallons):
    mpg = (miles / gallons)

    return mpg

# Calculations
while True:
    destination_city = str(input("Enter Destination City (Enter QUIT to end): "))

    if destination_city == "QUIT":
        break
    
    # Miles and Gallons Entered by User
    miles = float(input("Enter Miles: "))
    gallons = float(input("Enter Gallons: "))


    # MPG With Function
    mpg = mpg_function(miles, gallons)

    # Trip Counter
    number_of_trips = number_of_trips + 1

    # Display 1
    print("Destination City: ", destination_city)
    print("Miles: ", miles)
    print("Miles Per Gallon: ", mpg)

# Display 2
print()
print("Amount of Trips: ", number_of_trips)
