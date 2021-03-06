def convert_unit(desired_unit, answer):
    unit_list = ["km", "", "", "m", "", "cm", "mm"]
    number_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    if answer[len(answer)-1] in number_list:
        num = answer
        unit = desired_unit
    else:
        num = answer[:len(answer)-1]
        unit = answer[len(answer)-1]
        if answer[len(answer)-2] not in number_list:
            num = answer[:len(answer)-2]
            unit = answer[len(answer)-2:]

    index1 = unit_list.index(unit)
    index2 = unit_list.index(desired_unit)
    
    num = int(num)
    power = int(index2 - index1)

    converted_num = num*(10**power)
    return "{}{}".format(converted_num, desired_unit)
    
# Main Routine

what_unit = input("Unit: ")
length = input("Length: ")
conversion = convert_unit(what_unit, length)

print(conversion)