# Christopher Monarrez M9P5

# Variables
total_tuition_owed = 0


# Calculations

# Defining Tuition Function
def tuition_function(credit_hours, district_code):
    if district_code == "I":
        tuition = (credit_hours * 250)
    elif district_code == "O":
        tuition = (credit_hours * 550)

    return tuition


# While Loop
while True:
    # Student Last Name Entered by User
    student_last_name = input("Enter Student Last Name (Enter QUIT to end): ")

    if student_last_name == "QUIT":
        break

    # Credit Hours and District Codes Entered by User
    credit_hours = int(input("Enter Credit Hours: "))
    district_code = str(input("Enter District Code (I or O): "))


    # Tuition
    tuition = tuition_function(credit_hours, district_code)

    # Total Tuition Owed
    total_tuition_owed = total_tuition_owed + tuition

    # Display 1
    print("Student Last Name: ", student_last_name)
    print("Tuition Owed", tuition)


# Display 2
print()
print("Total Tuition That is Owed: ", total_tuition_owed)