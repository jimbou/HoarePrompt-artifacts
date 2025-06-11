#State of the program right berfore the function call: n is a positive integer, m is a non-negative integer, and nums is a list of n positive integers.
    tot = sum(len(val) for val in map(str, nums))
    cntvals = sorted((zerocnts(val) for val in nums), reverse=True)
    for i in range(0, len(cntvals), 2):
        tot -= cntvals[i]
        
    #State: n is a positive integer, m is a non-negative integer, nums is a list of n positive integers, tot is the sum of the lengths of the string representations of all integers in nums minus the sum of the counts of zeros in the string representations of the integers in nums at even indices, cntvals is a list of the counts of zeros in the string representations of the integers in nums, sorted in descending order and must have at least ceil(len(cntvals)/2) elements, i is the largest even number less than or equal to len(cntvals)
    return 'Sasha' if tot >= m + 1 else 'Anna'
    #The program returns either 'Sasha' or 'Anna'. 'Sasha' is returned if the total sum of the lengths of the string representations of all integers in 'nums' minus the sum of the counts of zeros in the string representations of the integers in 'nums' at even indices is greater than or equal to 'm + 1', otherwise 'Anna' is returned. Here, 'm' is a non-negative integer.

#Overall this is what the function does:This function determines the winner of a game based on the sum of the lengths of the string representations of a list of positive integers, minus the sum of the counts of zeros in the string representations of the integers at even indices. It returns 'Sasha' if this total sum is greater than or equal to a given non-negative integer 'm' plus one, otherwise it returns 'Anna'.

#State of the program right berfore the function call: num is a non-negative integer.
    num = str(num)
    tot = 0
    for i in range(len(num) - 1, -1, -1):
        if num[i] != '0':
            break
        
        tot += 1
        
    #State: num is a string representing a non-negative integer, tot is the number of trailing zeros in num, and i is -1
    return tot
    #The program returns the number of trailing zeros in the string 'num' that represents a non-negative integer.

#Overall this is what the function does:Counts and returns the number of trailing zeros in a given non-negative integer, represented as a string.

