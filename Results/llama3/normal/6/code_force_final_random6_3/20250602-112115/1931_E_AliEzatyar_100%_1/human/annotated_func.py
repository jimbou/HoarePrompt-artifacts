#State of the program right berfore the function call: num is a string of digits.
    counter = 0
    for i in range(len(num) - 1, -1, -1):
        if num[i] == '0':
            counter += 1
        else:
            break
        
    #State: `num` is a string of digits, `counter` is the number of trailing zeros in `num`.
    return counter
    #The program returns the number of trailing zeros in the string of digits 'num'.

#Overall this is what the function does:Counts and returns the number of trailing zeros in a given string of digits.

