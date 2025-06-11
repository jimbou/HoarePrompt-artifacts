#State of the program right berfore the function call: n is a positive integer, m is a non-negative integer, and nums is a list of n positive integers.
    tot = sum(len(val) for val in map(str, nums))
    cntvals = sorted((zerocnts(val) for val in nums), reverse=True)
    for i in range(0, len(cntvals), 2):
        tot -= cntvals[i]
        
    #State: Output State: n is a positive integer, m is a non-negative integer, nums is a list of n positive integers, tot is the sum of the number of digits in all integers in nums minus the number of zeros in every other integer in nums (starting from the integer with the most zeros), cntvals is a list of the number of zeros in each integer in nums, sorted in descending order.
    return 'Sasha' if tot >= m + 1 else 'Anna'
    #The program returns either 'Sasha' or 'Anna'. 'Sasha' is returned if the total number of digits in all integers in 'nums' minus the number of zeros in every other integer in 'nums' (starting from the integer with the most zeros) is greater than or equal to 'm + 1', where 'm' is a non-negative integer. 'Anna' is returned otherwise.

#Overall this is what the function does:This function determines the winner of a game based on the number of digits in a list of integers and the number of zeros in every other integer. It takes as input a list of positive integers and a non-negative integer, and returns either 'Sasha' or 'Anna' depending on whether the total number of digits minus the number of zeros in every other integer is greater than or equal to the input non-negative integer plus one.

#State of the program right berfore the function call: num is a non-negative integer
    num = str(num)
    tot = 0
    for i in range(len(num) - 1, -1, -1):
        if num[i] != '0':
            break
        
        tot += 1
        
    #State: Output State: num is a string representing a non-negative integer, tot is the number of trailing zeros in num.
    return tot
    #The program returns the number of trailing zeros in the string 'num' that represents a non-negative integer.

#Overall this is what the function does:Counts and returns the number of trailing zeros in a given non-negative integer.

