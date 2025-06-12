#State of the program right berfore the function call: stdin contains two inputs: first an integer t (1 <= t <= 50) and then t integers n (2 <= n <= 10^3).
    for i in range(0, int(input())):
        n = int(input())
        
        print(1, 1)
        
        print(1, 2)
        
        for i in range(3, n + 2):
            print(i, i)
        
    #State: `n` is an integer between 1 and 50 (inclusive), `i` is `t` and the numbers from 1 to `n + 1` (inclusive) are printed `t` times each.

#Overall this is what the function does:This function reads a series of integers from standard input, where the first integer represents the number of test cases (t) and each subsequent integer (n) represents the number of times to print a sequence of numbers from 1 to n+1. The function then prints the sequence of numbers for each test case, with each number printed on a new line. The function does not return any value, but rather prints the output directly to the console.

