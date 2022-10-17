calculation_to_unit = 24
name_of_unit = 'hours'


def days_to_units(num_of_days):
     return f"{num_of_days} days are {num_of_days * calculation_to_unit} {name_of_unit}"


def validate_and_execute():
    try:
        user_input_number = int(user_input)
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print("Your input is a 0, please put positive number!")
        else:
            print("Your input is a negative number, no conversion for you!")
    except ValueError:
            print("Your input is not a valid number, don't ruin my app!")


user_input = ""
while user_input != "exit":
    user_input = input("Hej, enter a numer of days and I will convert it to hours!\n")
    validate_and_execute()