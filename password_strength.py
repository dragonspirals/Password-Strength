# ---------------------------------------------------------------------------- #
#                               PASSWORD CHECKER                               #
# ---------------------------------------------------------------------------- #

# checks if a password is strong


# counts the number of each type of character in the sttring
def count_string(string):

    
    # dictionary of character types - {type name: num of chars}
    char_type = {
    "num": 0,
    "upper": 0,
    "lower": 0,
    "special": 0,
    "space": 0,
    "other": 0,
    }


    
    for char in string:


        # spaces
        if char == " ":
            char_type["space"] += 1

            
        # alphabetic
        elif char.isalpha(): 

            # uppercase
            if char.isupper():
                char_type["upper"] +=1

            # lowercase
            elif char.islower():
                char_type["lower"] +=1

            # something else? 
            else:
                char_type["other"] +=1
                

        # numeric 
        elif char in "0123456789": 
            char_type["num"] += 1

        # special
        elif char in  "!\"#$%&'()*+,-./:;<=>?@\\^_`{|}~":
            char_type["special"] += 1

        # other 
        else:
            char_type["other"] += 1
        
    return char_type




def check_password(password):

    char_type = count_string(password)

    message = ""
    password_strength = 0
    # check for invalid characters add 1 for each valid char type 



# --------------------------- Character types used --------------------------- #
    # spaces


    
    types_used = 0



    #  spaces
    if char_type["space"] > 0:
        message += "\nSpaces are not allowed\n"
        return message
    
    # weird characters
    if char_type["other"] > 0:
        message += "\nYou have used an invalid character\n"
        return message
    

    message += "\nCharacter types used:\n"

    # numerical characters
    message += "- Numerical: \t"
    if char_type["num"] > 0:
        password_strength += 1
        message += "Yes\n"
    else:
        message += "No\n"

    # lowercase
    message += "- Lowercase: \t"
    if char_type["lower"] > 0:
        password_strength += 1
        message += "Yes\n"
    else:
        message += "No\n"

    # uppercase
    message += "- Uppercase: \t"
    if char_type["upper"] > 0:
        password_strength += 1
        message += "Yes\n"
    else:
        message += "No\n"


    # special
    message += "- Special: \t"
    if char_type["special"] > 0:
        password_strength += 1
        message += "Yes\n"
    else:
        message += "No\n"



# ------------------------------ password length ----------------------------- #

    if len(password) > 14:
        password_strength += 3
    elif len(password) > 12:
        password_strength += 2
    elif len(password) > 10:
        password_strength += 1
    else:
        message += "Password must contain at least 8 characters\n"
        return


    if password_strength >= 6:
        message += "\nPassword Strength: Strong\n"
    elif password_strength >= 4:
        message += "\nPassword Strength: Moderate\n"
    elif password_strength >= 2:
        message += "\nPassword Strength: Poor\n"
    else: message += "\nPassword Strength: Very Poor\n"


    return message

    

# ------------------------------------ run ----------------------------------- #
#  asks for password input, prints password strength, asks to run again

print("""----- PASSWORD STRENGTH CHECK -----""")


while True: 
    password = input("Please enter a password: ")

    print(check_password(password))

    run_again = input("Would you like to check another password? (type Y/N): ").lower()

    if run_again == "y":
        continue
    elif run_again == "n":
        break
    else:
        print("Sorry, I do not understand")

