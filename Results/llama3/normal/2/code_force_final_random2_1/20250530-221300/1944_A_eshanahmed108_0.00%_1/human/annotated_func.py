#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t lines, each containing two integers n and k (1 <= n <= 100, 0 <= k <= n*(n-1)/2).
    for _ in range(int(input())):
        n, k = map(int, input().split())
        
        print(n if n - k <= 1 else 1)
        
    #State: The loop will execute until there is no more input in stdin. For each iteration, it will read two integers n and k from stdin, and print n if n is less than or equal to k + 1, otherwise it will print 1. After all iterations, stdin will be empty.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of two integers n and k. For each test case, it prints the value of n if n is less than or equal to k + 1, otherwise it prints 1. The function continues to read and process test cases until all input has been consumed from standard input, leaving it empty.

