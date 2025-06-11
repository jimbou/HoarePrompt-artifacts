#State of the program right berfore the function call: num is an integer (1 <= num <= 10^4).
    counter = 0
    for i in range(len(num) - 1, -1, -1):
        if num[i] == '0':
            counter += 1
        else:
            break
        
    #State: `num` is an integer (1 <= num <= 10^4) and is greater than 0, `i` is -1, `counter` is either 0 or equal to the number of trailing zeros in `num`.
    return counter
    #The program returns the number of trailing zeros in the integer 'num', which is either 0 or equal to the number of trailing zeros in 'num'.

#Overall this is what the function does:This function takes an integer 'num' as input and returns the number of trailing zeros in its decimal representation. The function accepts integers between 1 and 10^4 and returns a value that is either 0 or equal to the number of trailing zeros in the input integer.

