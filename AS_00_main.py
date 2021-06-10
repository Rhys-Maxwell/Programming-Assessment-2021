# Number checker function goes here
# Ensures user enters a valid number
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
# Ensure users answer is valid
def string_checker(choice, options, error):
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