# string checking functions, takes in
# question and list of valid responses
def string_checker(question, to_check):

    valid = False
    while not valid:

        response = input(question).lower()

        if response in to_check:
            return response

        else:
            for item in to_check:
                # checks if response is the first letter of
                # an item in the list
                if response == item[0]:
                    # note: returns the entire response
                    # rather than just the first letter
                    return item

        print("sorry that is not a valid response")

instructions = "test instructions"

#  *** Main Routine Goes Here ***
for item in range (0, 6):
    used_program = string_checker ("Have you used this program before?", ["yes", "no"])
    print("Answer: ", used_program)
    print()

    if used_program == "Yes":
        print("User knows how to use program")

    if used_program == "No":
        print(instructions)

    else:
        print("Sorry, you must answer yes / no")

