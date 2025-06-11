#State of the program right berfore the function call: x is a list of two integers, the first integer is greater than or equal to the second integer, and the second integer is greater than 0.
    output1 = []
    output2 = []
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            output1.append(i)
            output2.append(int(x / i))
        
    #State: x is a list of two integers, the first integer is greater than or equal to the second integer, and the second integer is greater than 0. output1 is a list containing all the divisors of the first integer in x that are less than or equal to the square root of the first integer. output2 is a list containing the integer division of the first integer in x by each of the divisors in output1.
    output1.reverse()
    return output2 + output1
    #The program returns a list that contains the integer division of the first integer in x by each of the divisors in output1, followed by all the divisors of the first integer in x that are less than or equal to the square root of the first integer, in reverse order.

#Overall this is what the function does:This function takes a list of two integers as input, where the first integer is greater than or equal to the second integer, and the second integer is greater than 0. It calculates the divisors of the first integer that are less than or equal to its square root, and their corresponding integer divisions. The function returns a list containing the integer divisions in the order they were calculated, followed by the divisors in reverse order.

