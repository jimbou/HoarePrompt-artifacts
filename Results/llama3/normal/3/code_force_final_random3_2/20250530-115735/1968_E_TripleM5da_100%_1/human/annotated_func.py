#State of the program right berfore the function call: stdin contains two inputs: first an integer (1 <= t <= 50) and then t lines each containing an integer (2 <= n <= 10^3).
    for i in range(0, int(input())):
        n = int(input())
        
        print(1, 1)
        
        print(1, 2)
        
        for i in range(3, n + 1):
            print(i, i)
        
    #State: `i` is `n + 1`, `n` is an integer between 2 and 10^3, stdin is empty, and this is printed: 1, 2, and then `n - 1` pairs of identical integers from 3 to `n`, and this is printed: 1, 1, and 1 and 2 are printed, and all pairs of identical integers from 3 to `n` are printed, and this is repeated `t` times.

#Overall this is what the function does:The function reads a series of integers from standard input, where the first integer represents the number of test cases (t), and each subsequent integer represents the number of pairs to be printed (n). For each test case, the function prints a specific pattern of pairs: (1, 1), (1, 2), and then n-1 pairs of identical integers from 3 to n. This pattern is repeated t times, and the function consumes all input from standard input.

