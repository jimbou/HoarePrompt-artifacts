#State of the program right berfore the function call: num is an integer (1 ≤ num ≤ 10^4).
    counter = 0
    for i in range(len(num) - 1, -1, -1):
        if num[i] == '0':
            counter += 1
        else:
            break
        
    #State: Output State: `num` is an integer (1 ≤ num ≤ 10^4), `counter` is the number of trailing zeros in the decimal representation of `num`.
    return counter
    #The program returns the number of trailing zeros in the decimal representation of the integer `num`, where `num` is an integer between 1 and 10^4 (inclusive).

#Overall this is what the function does:This function takes an integer `num` between 1 and 10^4 (inclusive) as input and returns the number of trailing zeros in its decimal representation. The function does not modify the input integer `num`. It only counts the trailing zeros and returns the count.

