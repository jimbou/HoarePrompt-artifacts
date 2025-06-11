#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t lines each containing an integer n (1 <= n <= 10^9).
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
        
    #State: The output state will be a list of integers, where each integer is the largest power of 2 that is less than or equal to the corresponding input integer n. If n is 1, the output will be 1. If n is a power of 2, the output will be n. Otherwise, the output will be the largest power of 2 that is less than n.

#Overall this is what the function does:This function reads a series of integers from standard input, where the first integer represents the number of test cases, and each subsequent integer represents a value 'n'. For each 'n', the function calculates and prints the largest power of 2 that is less than or equal to 'n'. If 'n' is 1, it prints 1. If 'n' is a power of 2, it prints 'n'. Otherwise, it prints the largest power of 2 less than 'n'. The function processes all test cases and outputs the results accordingly.

