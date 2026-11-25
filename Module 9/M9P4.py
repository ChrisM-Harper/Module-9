# Christopher Monarrez M9P4

# Variables
total_gross_pay = 0


# Calculations

# Defining JobCode Function
def pay_rate_function(jobcode):
    if jobcode == "L":
        rate = 25
    elif jobcode == "A":
        rate = 30
    elif jobcode == "J":
        rate = 50
        

    return rate


# While Loop
while True:
    employee_last_name = str(input("Enter Last Name (Enter QUIT to End): "))

    if employee_last_name == "QUIT":
        break

    # Job Code, Hours, and Rate
    jobcode = str(input("Enter Job Code (L, A, or J): "))
    hours = float(input("Enter Hours Worked: "))
    rate = pay_rate_function(jobcode)

    # If Statements for Hours 40 HR Work 
    if hours > 40:
        gross_pay = ((40 * rate) + (hours - 40) * rate * 1.5)
    else:
        gross_pay = (hours * rate)

    # Total Gross Pay to View After Loop Ends
    total_gross_pay = (total_gross_pay + gross_pay)


    # Display 1
    print("Employee Last Name: ", employee_last_name)
    print("Gross Pay: ", gross_pay)


# Display 2
print()
print("Total Gross Pay: ", total_gross_pay)



