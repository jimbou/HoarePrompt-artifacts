#State of the program right berfore the function call: num is an integer (1 <= num <= 10^4).
    counter = 0
    for i in range(len(num) - 1, -1, -1):
        if num[i] == '0':
            counter += 1
        else:
            break
        
    #State: Output State: The value of `counter` is equal to the number of trailing zeros in the string representation of `num`. The value of `num` remains unchanged.
    return counter
    #The program returns the number of trailing zeros in the string representation of `num`.

#Overall this is what the function does:This function takes an integer as input and returns the number of trailing zeros in its string representation, without modifying the original integer.

