#State of the program right berfore the function call: num is an integer (1 ≤ num ≤ 10^4) representing the number of test cases.
    counter = 0
    for i in range(len(num) - 1, -1, -1):
        if num[i] == '0':
            counter += 1
        else:
            break
        
    #State: Output State: The value of `counter` is the number of trailing zeros in the decimal representation of `num`.
    return counter
    #The program returns the number of trailing zeros in the decimal representation of `num`.

#Overall this is what the function does:This function takes an integer `num` as input and returns the number of trailing zeros in its decimal representation. It iterates through the digits of `num` from right to left, counting the number of consecutive zeros from the end. The function returns this count, effectively providing the number of trailing zeros in the decimal representation of the input integer.

