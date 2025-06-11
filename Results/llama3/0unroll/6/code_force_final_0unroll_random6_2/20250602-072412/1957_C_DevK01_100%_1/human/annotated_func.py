#State of the program right berfore the function call: n is a positive integer.
    dp = [1, 1]
    for i in range(2, n + 1):
        dp += [(dp[-1] + 2 * (i - 1) * dp[-2]) % (7 + 10 ** 9)]
        
        dp.pop(0)
        
    #State: Output State: `n` is a positive integer, `dp` is a list containing two elements, both equal to 1.
    return dp[-1]
    #The program returns the last element of the list 'dp', which is equal to 1.

#Overall this is what the function does:Calculates the nth Fibonacci number modulo 10^9 + 7, where n is a positive integer, and returns the result.

