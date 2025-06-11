#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t lines, each containing an integer n (1 <= n <= 10^9).
    n_cases = int(input())
    for i in range(n_cases):
        n = int(input())
        
        if n == 1:
            print(1)
        else:
            power = 1
            n = log2(n)
            while power < n:
                power += 1
            if power == n:
                print(2 ** power)
            else:
                power -= 1
                print(2 ** power)
        
    #State: `n_cases` is an integer between 0 and 10^4 (inclusive), `i` is `n_cases`, `n` is an integer between 1 and 10^9 (inclusive), stdin contains 0 lines. If `n` is 1, the number 1 is being printed. If `n` is greater than or equal to 2, `power` is either equal to `n` or `n-1`, and the value of 2 raised to the power of `power` is being printed. If `n` is greater than or equal to 2, `n` is updated to its base-2 logarithm, `power` is either equal to `n` or decreased by 1, and 2 raised to the power of either `n` or `power` is being printed, depending on whether `power` is equal to `n` or not, and 1 is printed. If `n` is greater than or equal to 2, `power` is equal to `n`, the value of 2 raised to the power of `n` is being printed. Otherwise, `power` is decreased by 1 and the value of 2 raised to the power of `power` is being printed.

#Overall this is what the function does:This function reads a series of integers from standard input, where the first integer represents the number of cases to follow. For each case, it reads an integer n and prints the largest power of 2 that is less than or equal to n. If n is 1, it simply prints 1. Otherwise, it calculates the base-2 logarithm of n and prints 2 raised to the power of either the logarithm or the logarithm minus 1, depending on which is less than or equal to n. The function continues this process until all cases have been processed, at which point the standard input is empty.

