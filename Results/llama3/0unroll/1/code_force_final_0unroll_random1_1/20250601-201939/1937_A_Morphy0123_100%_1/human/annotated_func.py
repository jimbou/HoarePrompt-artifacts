#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains a positive integer t. Each of the following t lines contains a positive integer n.
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
        
    #State: The loop will print the largest power of 2 that is less than or equal to the input number for each of the n_cases inputs. The value of n_cases will remain unchanged. The stdin will be empty after the loop finishes executing.

#Overall this is what the function does:The function reads a series of positive integers from standard input, where the first integer represents the number of cases (t) and each subsequent integer represents a value (n). For each value n, the function prints the largest power of 2 that is less than or equal to n. The function processes all input cases and leaves the standard input empty after execution.

