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
        
    #State: `n_cases` is an integer between 0 and 10^4 (inclusive), `i` is equal to `n_cases`, `n` is an integer, stdin contains 0 inputs. If `n` is 1, the number 1 is being printed. Otherwise, `n` is an integer equal to the base-2 logarithm of its original value, `power` is either equal to `n` or one less than its original value, and the value of 2 raised to the power of `power` is being printed. If `power` is equal to `n`, the value of 2 raised to the power of `power` (which is 2^n) is being printed. If `power` is not equal to `n`, `power` is one less than its original value and the value of 2 raised to the power of `power` (which is 2^(n-1)) is being printed. Additionally, if `n` is not 1, the number 1 is being printed.

#Overall this is what the function does:This function reads a series of integers from standard input, calculates the largest power of 2 that is less than or equal to each integer, and prints the result. If the input integer is 1, it simply prints 1. Otherwise, it calculates the base-2 logarithm of the integer, rounds down to the nearest whole number if necessary, and prints the corresponding power of 2. The function processes multiple test cases, with the number of cases specified by the first integer in the input.

