#State of the program right berfore the function call: num is an integer (1 <= num <= 10^4).
    counter = 0
    for i in range(len(num) - 1, -1, -1):
        if num[i] == '0':
            counter += 1
        else:
            break
        
    #State: `num` is a string representation of an integer with at least one digit, `i` is -1, and `counter` is the number of trailing zeros in `num`.
    return counter
    #The program returns the number of trailing zeros in the string representation of an integer 'num'

#Overall this is what the function does:Counts the number of trailing zeros in the string representation of an integer 'num' and returns this count. The function accepts a string 'num' and returns an integer representing the number of trailing zeros. The input string 'num' remains unchanged.

