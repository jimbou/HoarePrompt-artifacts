#State of the program right berfore the function call: stdin contains two inputs: two positive integers n and k such that 1 <= n <= 26 and 1 <= k <= 26.
    t = int(input())
    for i in range(t):
        n, k = map(int, input().split())
        
        print('abcdefghijklmnopqrstuvwxyz'[:k] * n)
        
    #State: `t` is at least `t`, `i` is `t-1`, `n` and `k` are the last two integers that were inputted, stdin contains no input, and this is printed: a string consisting of the first `k` characters of the alphabet repeated `n` times.

#Overall this is what the function does:The function reads a series of test cases from standard input, where each test case consists of two positive integers n and k. It then prints a string consisting of the first k characters of the alphabet repeated n times for each test case. The function consumes all input from standard input and does not return any value, only producing output to the console.

