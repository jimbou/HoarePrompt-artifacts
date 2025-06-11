#State of the program right berfore the function call: stdin contains two inputs: first an integer t (1 <= t <= 50) and then t integers n (2 <= n <= 10^3).
    for i in range(0, int(input())):
        n = int(input())
        
        print(1, 1)
        
        print(1, 2)
        
        for i in range(3, n + 1):
            print(i, i)
        
    #State: `i` is `n + 1`, `n` is an integer (1 <= n <= 50), stdin contains no input, and this is printed: 1, 2, 3, 3, 4, 4, 5, 5, ..., n, n.

#Overall this is what the function does:This function reads a series of integers from standard input, where the first integer t represents the number of subsequent integers n. For each n, it prints a sequence of pairs starting from (1, 1) and (1, 2), followed by pairs (i, i) for i ranging from 3 to n. The function repeats this process t times, consuming all input from standard input and producing a specific output pattern.

