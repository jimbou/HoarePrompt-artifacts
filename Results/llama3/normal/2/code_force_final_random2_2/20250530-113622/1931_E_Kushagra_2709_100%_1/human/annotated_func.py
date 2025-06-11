#State of the program right berfore the function call: n is a positive integer, m is a non-negative integer, nums is a list of n positive integers.
    tot = sum(len(val) for val in map(str, nums))
    cntvals = sorted((zerocnts(val) for val in nums), reverse=True)
    for i in range(0, len(cntvals), 2):
        tot -= cntvals[i]
        
    #State: n is a positive integer, m is a non-negative integer, nums is a list of n positive integers, tot is the sum of the number of digits in each integer in nums minus the sum of every other number of zeros in each integer in nums, cntvals is a list of the number of zeros in each integer in nums, sorted in descending order, and i is the largest even number less than or equal to the length of cntvals.
    return 'Sasha' if tot >= m + 1 else 'Anna'
    #The program returns either 'Sasha' or 'Anna'. If the total number of digits in the integers in 'nums' minus the sum of every other number of zeros in each integer in 'nums' is greater than or equal to the non-negative integer 'm' plus 1, then 'Sasha' is returned. Otherwise, 'Anna' is returned.

#Overall this is what the function does:Determines the winner of a game based on the total number of digits in a list of integers and the number of zeros in those integers. The function takes a list of positive integers and a non-negative integer as input, calculates the total number of digits minus the sum of every other number of zeros, and returns 'Sasha' if this total is greater than or equal to the non-negative integer plus 1, otherwise returns 'Anna'.

#State of the program right berfore the function call: num is a non-negative integer.
    num = str(num)
    tot = 0
    for i in range(len(num) - 1, -1, -1):
        if num[i] != '0':
            break
        
        tot += 1
        
    #State: `num` is a string representation of its original non-negative integer value, `tot` is the number of trailing zeros in `num`, `i` is -1.
    return tot
    #The program returns the number of trailing zeros in the string representation of a non-negative integer.

#Overall this is what the function does:Counts and returns the number of trailing zeros in the string representation of a non-negative integer.

