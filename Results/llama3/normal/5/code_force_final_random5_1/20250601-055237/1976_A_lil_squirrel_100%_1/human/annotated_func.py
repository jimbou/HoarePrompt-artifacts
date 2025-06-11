#State of the program right berfore the function call: n is a positive integer, password is a string of length n consisting of lowercase Latin letters and digits.
    letters = []
    digits = []
    for ch in password:
        if ch.isdigit():
            digits.append(ch)
        else:
            letters.append(ch)
        
    #State: n is a positive integer, password is an empty string, letters is a list of all lowercase Latin letters from the original password, digits is a list of all digits from the original password.
    if (letters != sorted(letters)) :
        return 'NO'
        #The program returns the string 'NO'
    #State: n is a positive integer, password is an empty string, letters is a list of all lowercase Latin letters from the original password, digits is a list of all digits from the original password, and the list of letters is sorted in ascending order.
    if (digits != sorted(digits)) :
        return 'NO'
        #The program returns the string 'NO'
    #State: *n is a positive integer, password is an empty string, letters is a list of all lowercase Latin letters from the original password, digits is a list of all digits from the original password, the list of letters is sorted in ascending order, and the list of digits is sorted in ascending order
    for i in range(len(password) - 1):
        if password[i].isalpha() and password[i + 1].isdigit():
            return 'NO'
        
    #State: n is a positive integer, password is a string with at least 2 characters, letters is a list of all lowercase Latin letters from the original password, digits is a list of all digits from the original password, the list of letters is sorted in ascending order, and the list of digits is sorted in ascending order, i is equal to the length of password minus 1. If the character at index i in password is a letter and the character at index i + 1 is a digit, the function returns 'NO'. Otherwise, no changes are made.
    return 'YES'
    #The program returns string 'YES'

#Overall this is what the function does:Checks if a given password meets certain conditions and returns 'YES' if it does, or 'NO' otherwise. The password is considered valid if it contains at least 2 characters, all lowercase Latin letters are in ascending order, all digits are in ascending order, and no letter is immediately followed by a digit.

