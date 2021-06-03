# Component 1a - make an integer checker for the base component

# Number checker function goes here
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


# Main Routine
height = number_checker("What is the height? ", "Sorry, You have to enter an integer more than 0", float)
base = number_checker("What is the base? ", "Sorry, You have to enter an integer more than 0", float)
area = height * base

print("{} x {} = {}".format(base, height, area))
print("The area is {}".format(area))