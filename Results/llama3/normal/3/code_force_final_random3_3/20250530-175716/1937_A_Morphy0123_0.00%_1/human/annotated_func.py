#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains an integer t (1 <= t <= 10^4) representing the number of test cases. Each of the following t lines contains one integer n (1 <= n <= 10^9) representing the length of the array a.
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
        
    #State: `n_cases` is an integer between 0 and 10^4 (inclusive), `i` is equal to `n_cases`, stdin contains no lines of input.

#Overall this is what the function does:The function reads a series of test cases from standard input, where each case consists of an integer representing the length of an array. For each case, it calculates and prints the largest power of 2 that is less than or equal to the given length, or 1 if the length is 1. The function processes all test cases and consumes all input from standard input, leaving no remaining input.

