#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t lines, each containing an integer n (1 <= n <= 10^9).
    n_cases = int(input())
    for i in range(n_cases):
        n = int(input())
        
        if n == 1:
            print(1)
        else:
            power = 1
            while power < log2(n):
                power += 1
            if power == n:
                print(2 ** power)
            else:
                power -= 1
                print(2 ** power)
        
    #State: `n_cases` is an integer between 1 and 10^4 (inclusive), `i` is `n_cases`, `n` is an integer between 1 and 10^9 (inclusive), stdin is empty. If `n` is 1, the number 1 is printed. If `n` is an integer greater than 2^30 and less than or equal to 10^9 (inclusive), either 2 raised to the power of 30 (1073741824) or 2 raised to the power of `power` (where `power` equals `n`) is printed.

#Overall this is what the function does:This function reads a series of integers from standard input, where the first integer represents the number of cases to follow. For each case, if the integer is 1, it prints 1. Otherwise, it calculates the largest power of 2 that is less than or equal to the integer and prints the result of 2 raised to that power. The function processes all cases and then terminates, leaving the standard input empty.

