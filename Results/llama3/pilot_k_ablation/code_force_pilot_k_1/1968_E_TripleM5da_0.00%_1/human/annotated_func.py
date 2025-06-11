#State of the program right berfore the function call: stdin contains two inputs: first an integer (t) (1 <= t <= 50) and then t integers (n) (2 <= n <= 10^3).
    for i in range(0, int(input())):
        n = int(input())
        
        print(1, 1)
        
        print(1, 2)
        
        for i in range(3, n + 2):
            print(i, i)
        
    #State: `i` is `t`, `n` is an integer (1 <= n <= 50), stdin contains no input, and this is printed: 1 2, followed by all numbers from 3 to `n + 1` printed twice, for each of the `t` integers.

#Overall this is what the function does:The function reads a series of integers from standard input, where the first integer (t) specifies the number of subsequent integers to read. For each of these subsequent integers (n), the function prints a sequence of numbers starting from 1 and 2, followed by all numbers from 3 to n+1, with each number printed twice. The function continues this process until all t integers have been processed, at which point standard input is exhausted.

