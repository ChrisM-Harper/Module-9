# Christopher Monarrez M9P2

# Variables
number_of_players_entered = 0


# Calculations

# Defining Averages function
def batting_average(hits, at_bats):
    avg = (hits / at_bats)

    return avg


# While Loop
while True:
    players_last_name = str(input("Enter Player's Last Name (Enter QUIT to end): "))

    if players_last_name == "QUIT":
        break

    # Hits and At Bats Entered by User
    hits = int(input("Enter Number of Hits: "))
    at_bats = int(input("Enter Number of At Bats: "))

    # Average With function
    avg = batting_average(hits, at_bats)

    # Adding to Player Count at the End
    number_of_players_entered + 1

    # Display 1
    print("Players last Name: ", players_last_name)
    print("Batting Average: ", avg)

# Display 2
print()
print("Total Player Count: ", number_of_players_entered)

