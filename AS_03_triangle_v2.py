import math


# string_checker function goes here
# Ensures that an input is within the possible results
def string_checker(choice, options, error):
    is_valid = ""
    chosen = ""

    for var_list in options:

        # if the shape is in one of the lists, return the full list
        if choice in var_list:

            # Get full name of shape and put it in title case
            chosen = choice.title()
            is_valid = "yes"
            break

        # if the chosen shape is not valid, set is_valid to no
        else:
            is_valid = "no"

    # If shape is not OK - ask question again
    if is_valid == "yes":
        return chosen
    else:
        print(error + "\n")
        return "invalid choice"



# triangle function goes here
# Asks user what they want for there shape and calculates the area and perimeter
def triangle(info_type, result):
    valid = False
    while not valid:

        # User has given base and height
        if info_type == "Bh":

            # Inform user cant be calculated
            if result == "perimeter":
                print("Sorry, I can't find the perimeter with only base and height, Please enter more information")
                return "Unable to calculate"
            # Ask user for base height and length
            else:
                base = float(input("What is the base length? "))
                height = float(input("What is the height? "))

                area = 0.5 * base * height
                print("The area of your triangle is {}".format(area))
                # return for future use
                return ("triangle", base, height, area)

        # User has entered all triangle sides
        else:
            a = float(input("What is the length of a? "))
            b = float(input("What is the length of b? "))
            c = float(input("What is the length of c? "))

            # Give user the area of there shape
            if result == "area":
                s = (a + b + c) / 2
                area = math.sqrt(s * (s - a) * (s - b) * (s - c))
                print("The area of your triangle is {}".format(area))
                # return for future use
                return ("triangle", a, b, c, area)
            # Give user the perimeter of there shape
            else:
                perimeter = a + b + c
                print("The area of your triangle is {}".format(perimeter))
                # return for future use
                return ("triangle", a, b, c, perimeter)


# Main Routine

# Shape types
shape_types = ["square", "rectangle", "parallelogram", "triangle", "circle",]

# Ask user for shape
what_shape = input("Please enter a shape ").lower()
check_shape = string_checker(what_shape, shape_types, "Please enter a valid shape")

# Triangle
if check_shape == "Triangle":
    # Ask user for Area or Perimeter
    triangle_outcome = input("Do you want to find the Area or Perimeter? ").lower()
    triangle_outcome_check = string_checker(triangle_outcome, ["area", "perimeter"],
                                            "This must be either Area or Perimeter")
    print()

    # Ask user for infomation about the tirangle
    triangle_info = input("What do you know about the triangle (bh or abc)? ")
    triangle_info_check = string_checker(triangle_info, ["bh", "abc"],
                                         "Please enter either 'bh' for base and height or 'abc' for side lengths")
    triangle_calc = triangle(triangle_info_check, triangle_outcome)