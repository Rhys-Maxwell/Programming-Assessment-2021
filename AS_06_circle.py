import math

# number checker function goes here
# Checks that it is not 0 and is a number
def number_checker(question, error, num_type):
    valid = False
    while not valid:

        try:
            response = num_type(input(question))
        
            if response <= 0:
                print(error)
            else:
                return response

        except ValueError:
            print(error)

# string_checker function goes here
# Ensures that an input is within the possible results
def string_checker(choice, options, error):
    for var_list in options:

        # Blank case
        if choice == "":
            is_valid = "no"
            break 
        # if the shape is in one of the lists, return the full list
        elif choice in var_list:

            # Get full name of shape and put it in title case
            # so it looks nice when out putted
            chosen = var_list[0].title()
            is_valid = "yes"
            break

        # if the chosen shape is not valid
        else:
            is_valid = "no"

    # If shape is not OK - ask question again
    if is_valid == "yes":
        return chosen
    else:
        print(error)
        return "invalid choice"

# circle function goes here
# Find the radius or diameter then calculate area and circumference
def circle():
    valid = False
    while not valid:

        radius = number_checker("What is the radius? ", "Please enter a number above 0", float)
        
        # ------------- Calculations -------------
        circumference = 2 * (math.pi) * radius
        area = (math.pi) * radius**2

        print("The area of your circle is {:.2f}".format(area))
        print("The circumference of your circle is {:.2f}".format(circumference))
        print()

        # return this until I put in a list for history
        return ""

# Main Routine

what_shape = "circle"

for item in range(0,1):
    if what_shape == "circle":
        result = circle()