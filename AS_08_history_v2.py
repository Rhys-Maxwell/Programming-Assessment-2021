import math
import pandas

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

# get_shape function goes here
# get the desired shape
def get_shape():

    # Possible Shapes
    valid_shapes = [["square", "squ", "s"],
                    ["rectangle", "rec", "r"],
                    ["triangle", "tri", "t"],
                    ["circle", "cir", "c"],
                    ["parallelogram", "par", "p"],
                    ["trapezium", "tra", "t"]]

    valid = False
    while not valid:

        # Find the shape
        desired_shape = input("What shape do you want? ").lower()
        check_shape = string_checker(desired_shape, valid_shapes, "Please enter a real shape")

        # When invalid choice
        if check_shape == "invalid choice":
            continue
        # t can be either triangle or trapezium so ask to specify
        elif desired_shape == "t":
            print("Can you specify either triangle or trapezium\n")
            continue
        else:
            break

    return check_shape

# rectangle function goes here
# Find the base and height then calculate area and perimeter
def rectangle():
    valid = False
    while not valid:
        
        # Get base and height
        base = number_checker("What is the base? ", "Please enter a number above 0", float)
        height = number_checker("What is the height? ", "Please enter a number above 0", float)
        recorded_info = ("Base: {} | Height: {}".format(base, height))

        # ------------- Calculations -------------
        area = base * height
        perimeter = (2 * base) + (2 * height)

        # Check if it is a square
        if base == height:
            squ_or_rec = "square"
        else:
            squ_or_rec = "rectangle"

        # Print with appropriate shape name
        print("The area of your {} is {:.2f}".format(squ_or_rec, area))
        print("The perimeter of your {} is {:.2f}".format(squ_or_rec, perimeter))

        # return this for use in history
        return ["Rectangle", area, perimeter, recorded_info]

# triangle function goes here
# Figures out what the question gives and calculates the area and perimeter
def triangle():

    valid = False
    while not valid:

        # Find what the user is given
        info = input("What do you know about the triangle [Base and height(bh)] or [the side lengths(abc)]? ").lower()
        info_check = string_checker(info, [["bh"], ["abc"]], "Please say either 'bh' for base and height or 'abc' for side lengths")
        if info_check == "invalid choice":
            continue

        # ------------- Calculations -------------
        # If base and height is given
        if info_check == "Bh":

            # Find Base and height
            base = number_checker("What is the base? ", "Please enter a number bigger than 0", float)
            height = number_checker("What is the height? ", "Please enter a number bigger than 0", float)
            recorded_info = ("Base: {} | Height: {}".format(base, height))
                
            area = 0.5 * base * height
            perimeter = "couldn't find"

            print("The area of your triangle is {:.2f}".format(area))
            print("I can't find the perimeter with only base and height")

        # If triangle side lengths are given
        else:
            # Find triangle side lengths
            a = number_checker("What is the length of a? ", "Please enter a number bigger than 0", float)
            b = number_checker("What is the length of b? ", "Please enter a number bigger than 0", float)
            c = number_checker("What is the length of c? ", "Please enter a number bigger than 0", float)
            recorded_info = ("A: {} | B: {} | C: {}".format(a, b, c))

            # Do Heron's Law and the sum of all the side lengths for perimeter
            s = (a + b + c) / 2
            perimeter = a + b + c
            area = math.sqrt(s * (s-a) * (s-b) * (s-c))

            print("The area of your triangle is {:.2f}".format(area))
            print("The perimeter of your triangle is {:.2f}".format(perimeter))

        # return this for use in history
        return ["Triangle", area, perimeter, recorded_info]

# circle function goes here
# Find the radius or diameter then calculate area and circumference
def circle():
    valid = False
    while not valid:
        
        # Find what the user is given
        info = input("What do you know about the circle [radius(r)] or [diameter(d)]? ").lower()
        info_check = string_checker(info, [["r"], ["d"]], "Please say either 'r' for radius or 'd' for diameter")
        if info_check == "invalid choice":
            continue

        # Diameter case
        if info_check.lower() == "d":
            diameter = number_checker("What is the diameter? ", "Please enter a number above 0", float)
            # radius is diameter divided by 2
            r = diameter / 2
            recorded_info = ("Diameter: {}".format(diameter))
        # Radius Case
        else:
            radius = number_checker("What is the radius? ", "Please enter a number above 0", float)
            r = radius
        recorded_info = ("Radius: {}".format(r))

        # ------------- Calculations -------------
        circumference = 2 * (math.pi) * r
        area = (math.pi) * r**2

        print("The area of your circle is {:.2f}".format(area))
        print("The circumference of your circle is {:.2f}".format(circumference))
        print()

        # return this for use in history
        return ["Circle", area, circumference, recorded_info]

# parallelogram function goes here
# Find the base, height and side length then calculate area and perimeter
def parallelogram():
    valid = False
    while not valid:

        # Find what the user is looking for
        info = input("What do you want to find out [Area(a)] or [Perimeter(p)] or [Both(ap)]? ").lower()
        info_check = string_checker(info, [["a "], [" p"], ["ap"]], "Please say either 'a' for area or 'p' for perimeter")
        if info_check == "invalid choice":
            continue
        
        # base is needed in all cases so it is outside the if statement
        base = number_checker("What is the base? ", "Please enter a number above 0", float)
        # Check if user wants area
        if info_check[0] == "A":
            height = number_checker("What is the height? ", "Please enter a number above 0", float)
            # Check if user wants perimeter as well
            if info_check[1] == "p":
                side = number_checker("What is the side length? ", "Please enter a number above 0", float)
                recorded_info = ("Base: {} | Height: {} | Side: {}".format(base, height, side))
            # If only area
            else:
                side = 0
                recorded_info = ("Base: {} | Height: {}".format(base, height))
        # Perimeter scenario
        else:
            side = number_checker("What is the side length? ", "Please enter a number above 0", float)
            height = 0
            recorded_info = ("Base: {} | Side: {}".format(base, side))
        
        # ------------- Calculations -------------
        area = base * height
        perimeter = 2 * (side + base)

        # Area
        if height != 0:
            print("The area of your parallelogram is {:.2f}".format(area))
            # Perimeter as well
            if side != 0:
                print("The perimeter of your parallelogram is {:.2f}".format(perimeter))
        # Perimeter only
        else:
            print("The perimeter of your parallelogram is {:.2f}".format(perimeter))
        print()
        # return this for use in history
        return ["Parallelogram", area, perimeter, recorded_info]

# trapezium function goes here
# Find the base, height and side length then calculate area and perimeter
def trapezium():
    valid = False
    while not valid:

        # Find what the user is looking for
        info = input("What do you want to find out [Area(a)] or [Perimeter(p)] or [Both(ap)]? ").lower()
        info_check = string_checker(info, [["a "], [" p"], ["ap"]], "Please say either 'a' for area or 'p' for perimeter")
        if info_check == "invalid choice":
            continue
        
        # base is needed in all cases so it is outside the if statement
        base_a = number_checker("What is the first base? ", "Please enter a number above 0", float)
        base_b = number_checker("What is the second base? ", "Please enter a number above 0", float)
        # Check if user wants perimeter
        if info_check[1] == "p" or info_check[1] == "P":
            side_c = number_checker("What is the first side length? ", "Please enter a number above 0", float)
            side_d = number_checker("What is the second side length? ", "Please enter a number above 0", float)
            # Check if user wants perimeter as well
            if info_check[0] == "A":
                height = number_checker("What is the height? ", "Please enter a number above 0", float)
                recorded_info = ("A: {} | B: {} | C: {} | D: {} | Height: {}".format(base_a, base_b, side_c, side_d, height))
            # If only area
            else:
                height = 0
                recorded_info = ("A: {} | B: {} | C: {} | D: {}".format(base_a, base_b, side_c, side_d))
        # Perimeter scenario
        else:
            height = number_checker("What is the height? ", "Please enter a number above 0", float)
            side_c = 0
            side_d = 0
            recorded_info = ("A: {} | B: {} | Height: {}".format(base_a, base_b, height))
        
        # ------------- Calculations -------------
        area = ((base_a + base_b)/2) * height
        perimeter = base_a + base_b + side_c + side_d

        # Area
        if height != 0:
            print("The area of your trapezium is {:.2f}".format(area))
            # Perimeter as well
            if side_c != 0:
                print("The perimeter of your trapezium is {:.2f}".format(perimeter))
        # Perimeter only
        else:
            print("The perimeter of your trapezium is {:.2f}".format(perimeter))
        print()
        # return this for use in history
        return ["Trapezium", area, perimeter, recorded_info]

# Main Routine
history = []

# Keep going loop
keep_going = ""
while keep_going == "":
    what_shape = get_shape()

    # Only rectangle and triangle for testing purposes
    if what_shape == "Rectangle" or what_shape == "Square":
            result = rectangle()
    else:
        result = triangle()

    # Append results to a history lsit for later printing
    history.append(result)
    keep_going = input("\nIf you want to continue press enter or any other key to quit: ")

print()
print("=============== History ===============\n")
# Make a dataframe
history_frame = pandas.DataFrame(history, columns=["Shape", "Area", "Perimeter", "Info"])

print(history_frame)
print()