#State of the program right berfore the function call: n is a positive integer, m is a non-negative integer, and nums is a list of n positive integers.
    tot = sum(len(val) for val in map(str, nums))
    cntvals = sorted((zerocnts(val) for val in nums), reverse=True)
    for i in range(0, len(cntvals), 2):
        tot -= cntvals[i]
        
    #State: n is a positive integer, m is a non-negative integer, nums is a list of n positive integers, tot is the total number of digits in all integers in nums minus the sum of the counts of zeros in the integers with the most zeros, the third most zeros, the fifth most zeros, and so on, in nums, cntvals is a list of the counts of zeros in the integers in nums, sorted in descending order, and i is the largest even number less than or equal to the length of cntvals.
    return 'Sasha' if tot >= m + 1 else 'Anna'
    #The program returns either 'Sasha' or 'Anna'. If the total number of digits in all integers in nums minus the sum of the counts of zeros in the integers with the most zeros, the third most zeros, the fifth most zeros, and so on, in nums is greater than or equal to m + 1, the program returns 'Sasha'. Otherwise, the program returns 'Anna'.

#Overall this is what the function does:This function determines the winner of a game based on the total number of digits in a list of integers and the count of zeros in those integers. It takes three inputs: a positive integer n, a non-negative integer m, and a list of n positive integers. The function calculates the total number of digits in all integers, subtracts the sum of the counts of zeros in the integers with the most zeros, the third most zeros, the fifth most zeros, and so on, and compares the result to m + 1. If the result is greater than or equal to m + 1, the function returns 'Sasha', indicating Sasha wins. Otherwise, it returns 'Anna', indicating Anna wins.

#State of the program right berfore the function call: num is a non-negative integer.
    num = str(num)
    tot = 0
    for i in range(len(num) - 1, -1, -1):
        if num[i] != '0':
            break
        
        tot += 1
        
    #State: num is a string representation of its original non-negative integer value, tot is the number of trailing zeros in num, i is -1
    return tot
    #The program returns the number of trailing zeros in the string representation of the original non-negative integer value of num.

#Overall this is what the function does:Counts and returns the number of trailing zeros in the string representation of a non-negative integer.

