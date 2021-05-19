# string checker to find out what shape user wants calculated

def string_check(choice, options):

    for var_list in options:

        # if the snack is in one of the lists, return the full snack name
        if choice in var_list:

            # Get the full name of the snack and put it in
            # title case so it looks nice when outputted
            chosen = var_list[0].title()
            is_valid = "yes"
            break

        # if the chosen option is not valid, set is_valid to no
        else:
            is_valid = "no"
    if is_valid == "yes":
        return chosen
    else:
        return "invalid choice"

# number checker to check if user has entered a whole number when asked questions that require a number value

def int_check(question, low_num, high_num):

    error = "Please  enter a whole number between {} " \
            "and {}".format(low_num, high_num)

    valid = False
    while not valid:

        # ask user for number and check it is valid
        try:
            response = int(input(question))

            if response <= 0:
                print(error)
            else:
                return error

        # if an integer is not entered, display an error
        except ValueError:
            print(error)

# hi