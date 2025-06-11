#State of the program right berfore the function call: n is a list of two non-negative integers.
    if (n == 0) :
        return -1
        #The program returns -1
    #State: *n is a list of two non-negative integers. The sum of the elements in n is not equal to 0
    position = 0
    while n != 0:
        n >>= 1
        
        position += 1
        
    #State: n is a list of two non-negative integers, where the first element is halved until it becomes 0, position is the number of times the first element of n was halved until it became 0.
    return position - 1
    #The program returns the number of times the first element of n was halved until it became 0, minus 1.

#Overall this is what the function does:This function calculates the number of times the first element of a list of two non-negative integers can be halved until it becomes 0, minus 1, or returns -1 if the input list is 0.

