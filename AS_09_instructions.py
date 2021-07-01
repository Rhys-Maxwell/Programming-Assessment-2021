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


# instructions funtion goes here
# Asks if user wants instructions then print accordingly
def instructions():
    # Title
    print("========== Welcome to the Area and Perimeter Calcualtor ==========\n")
    print(" 🤖 HENRYB⚙T: Hello, My Name is HENRYB⚙T\n")

    # Ask if user wants the instructions
  valid = False
    while not valid:
        need_instructions = input("Would you like to see the instructions? ").lower()
        need_instructions_check = string_checker(need_instructions, [["yes", "y"], ["no", "n"]],
                                                 "Please Enter Yes or No\n")
        if need_instructions_check == "invalid choice":
            continue

        if need_instructions_check == "No":

            return ""
        else:
            print()
            print("This program will calculate the area and perimeter of 5 shapes.\n"
                  "The available shapes are Triangle, Square, Rectangle, Circle and Parallelograms.\n"
                  "You can enter the first letter or the first three letters, eg. 't' or 'tri' for triangle.\n"
                  "or you can just put in the full name of your shape eg. 'Square'.")

            print()

            print(
                "Depending on what shape you do I will need different types of information or else I can't do the calculations so make sure you have it.\n")
            print(
                "After a calculation the program will ask if you want to enter another shape if so just press enter if you do, \n"
                "or put in any key then enter to stop. After you have stopped the code will print out a table of your calculations \n"
                "so you can go over them again.\n")
        # Return nothing because nothing is needed
        return ""


# Main Routine
# Call the instructions function
have_instruction = instructions()