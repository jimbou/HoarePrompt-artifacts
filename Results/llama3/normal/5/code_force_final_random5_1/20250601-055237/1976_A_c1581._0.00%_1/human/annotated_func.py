#State of the program right berfore the function call: password is a string consisting of lowercase Latin letters and digits.
    digits = []
    letters = []
    for char in password:
        if char.isdigit():
            digits.append(char)
        else:
            letters.append(char)
        
    #State: password is a string consisting of lowercase Latin letters and digits, char is the last character in the password. If char is a digit, digits is a list containing all the digits in the password, and letters is a list containing all the letters in the password. If char is a letter, digits is a list containing all the digits in the password, and letters is a list containing all the letters in the password.
    last_digit_index = -1
    for (i, char) in enumerate(password):
        if char.isdigit():
            last_digit_index = i
        elif last_digit_index != -1:
            return 'NO'
        
    #State: The password is a string consisting of lowercase Latin letters and digits. If the last character in the password is a digit, the last digit index is updated to the index of the last digit in the password. If the last character is not a digit and the last digit index is not -1, the program returns the string 'NO'. Otherwise, no changes are made to the variables.
    if (digits != sorted(digits)) :
        return 'NO'
        #The program returns the string 'NO'
    #State: The password is a string consisting of lowercase Latin letters and digits. If the last character in the password is a digit, the last digit index is updated to the index of the last digit in the password. If the last character is not a digit and the last digit index is not -1, the program returns the string 'NO'. Otherwise, no changes are made to the variables. The digits in the password are in ascending order.
    if (letters != sorted(letters)) :
        return 'NO'
        #The program returns the string 'NO'
    #State: *The password is a string consisting of lowercase Latin letters and digits. The digits in the password are in ascending order. The letters in the password are in ascending order. If the last character in the password is a digit, the last digit index is updated to the index of the last digit in the password. If the last character is not a digit and the last digit index is not -1, the program returns the string 'NO'. Otherwise, no changes are made to the variables.
    return 'YES'
    #The program returns 'YES'.

#Overall this is what the function does:Checks if a given password meets certain conditions and returns 'YES' if it does, or 'NO' otherwise. The password must consist of lowercase Latin letters and digits, with all digits in ascending order and all letters in ascending order. Additionally, if the last character is a digit, it must be the last digit in the password. If any of these conditions are not met, the function returns 'NO'.

