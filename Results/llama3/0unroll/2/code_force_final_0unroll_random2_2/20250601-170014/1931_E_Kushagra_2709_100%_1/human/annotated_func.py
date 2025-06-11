#State of the program right berfore the function call: n is a positive integer, m is a non-negative integer, and nums is a list of n positive integers.
    tot = sum(len(val) for val in map(str, nums))
    cntvals = sorted((zerocnts(val) for val in nums), reverse=True)
    for i in range(0, len(cntvals), 2):
        tot -= cntvals[i]
        
    #State: Output State: The value of tot is reduced by the sum of every other value in cntvals, starting from the first value (index 0), and the other variables remain unchanged.
    return 'Sasha' if tot >= m + 1 else 'Anna'
    #The program returns either 'Sasha' or 'Anna'. 'Sasha' is returned if the value of tot is greater than or equal to the value of m plus 1, otherwise 'Anna' is returned. The value of tot is reduced by the sum of every other value in cntvals, starting from the first value (index 0), and the other variables remain unchanged.

#Overall this is what the function does:This function determines the winner of a game based on the total count of digits in a list of numbers and a given threshold. It takes three inputs: a positive integer n, a non-negative integer m, and a list of n positive integers. The function calculates the total count of digits in the list of numbers, then reduces this total by the sum of every other value in a sorted list of digit counts, starting from the highest count. The function returns 'Sasha' if the reduced total is greater than or equal to the threshold m plus 1, and 'Anna' otherwise.

#State of the program right berfore the function call: num is a non-negative integer
    num = str(num)
    tot = 0
    for i in range(len(num) - 1, -1, -1):
        if num[i] != '0':
            break
        
        tot += 1
        
    #State: Output State: num is a string representation of its original non-negative integer value, tot is the number of trailing zeros in num.
    return tot
    #The program returns the number of trailing zeros in the string representation of the original non-negative integer value of num.

#Overall this is what the function does:Counts the number of trailing zeros in the string representation of a non-negative integer.

