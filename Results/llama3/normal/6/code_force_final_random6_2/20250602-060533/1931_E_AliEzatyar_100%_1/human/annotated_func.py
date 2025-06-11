#State of the program right berfore the function call: num is an integer (1 ≤ num ≤ 10^4).
    counter = 0
    for i in range(len(num) - 1, -1, -1):
        if num[i] == '0':
            counter += 1
        else:
            break
        
    #State: `num` is an integer with at least one digit, `i` is -1, `counter` is the number of trailing zeros in `num`.
    return counter
    #The program returns the number of trailing zeros in the integer 'num'.

#Overall this is what the function does:Counts and returns the number of trailing zeros in a given integer.

