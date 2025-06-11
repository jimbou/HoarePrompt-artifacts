#State of the program right berfore the function call: password is a string consisting of lowercase Latin letters and digits.
    digits = []
    letters = []
    for char in password:
        if char.isdigit():
            digits.append(char)
        else:
            letters.append(char)
        
    #State: Output State: The digits list contains all the digits from the password string, and the letters list contains all the lowercase Latin letters from the password string.
    last_digit_index = -1
    for (i, char) in enumerate(password):
        if char.isdigit():
            last_digit_index = i
        elif last_digit_index != -1:
            return 'NO'
        
    #State: Output State: The digits list contains all the digits from the password string, the letters list contains all the lowercase Latin letters from the password string, and last_digit_index is the index of the last digit in the password string.
    if (digits != sorted(digits)) :
        return 'NO'
        #The program returns the string 'NO'
    #State: The digits list contains all the digits from the password string, the letters list contains all the lowercase Latin letters from the password string, and last_digit_index is the index of the last digit in the password string. The digits list is sorted in ascending order.
    if (letters != sorted(letters)) :
        return 'NO'
        #The program returns the string 'NO'.
    #State: *The digits list contains all the digits from the password string, the letters list contains all the lowercase Latin letters from the password string, and last_digit_index is the index of the last digit in the password string. The digits list is sorted in ascending order. The letters list is sorted in ascending order.
    return 'YES'
    #The program returns the string 'YES'.

#Overall this is what the function does:Checks if a given password string meets certain conditions and returns 'YES' if it does, or 'NO' otherwise. The conditions are: (1) all digits in the password must be in ascending order, (2) all letters in the password must be in ascending order, and (3) all digits must come before all letters. If any of these conditions are not met, the function returns 'NO'. If all conditions are met, the function returns 'YES'.

