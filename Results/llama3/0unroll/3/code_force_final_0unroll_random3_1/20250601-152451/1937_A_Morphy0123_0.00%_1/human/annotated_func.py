#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) in the first line, followed by t lines each containing an integer n (1 <= n <= 10^9).
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
        
    #State: Output State: The output state after the loop executes all the iterations is a series of integers, each representing the largest power of 2 that is less than or equal to the corresponding input integer n. If n is a power of 2, the output is n itself. The number of output integers is equal to the initial value of `n_cases`.

#Overall this is what the function does:This function reads a series of integers from standard input, where the first integer represents the number of cases, and each subsequent integer represents a value for which the function calculates and prints the largest power of 2 that is less than or equal to the given integer. If the given integer is a power of 2, the function prints the integer itself. The function processes all cases and outputs the results in the same order as the input.

