#State of the program right berfore the function call: stdin contains two inputs: two positive integers n and k, such that 1 ≤ n ≤ 26 and 1 ≤ k ≤ 26.
    t = int(input())
    for i in range(t):
        n, k = map(int, input().split())
        
        print('abcdefghijklmnopqrstuvwxyz'[:k] * n)
        
    #State: `t` is a positive integer between 1 and 26 inclusive, `i` is equal to `t`, `n` is a positive integer between 1 and 26 inclusive, `k` is a positive integer between 1 and 26 inclusive, stdin is empty, and the first k characters of the string 'abcdefghijklmnopqrstuvwxyz' repeated n times is printed `t` times.

#Overall this is what the function does:The function reads a positive integer `t` from standard input, then reads `t` pairs of positive integers `n` and `k` (each between 1 and 26 inclusive) from standard input, and for each pair, it prints the first `k` characters of the alphabet repeated `n` times. After processing all pairs, the function leaves the standard input empty.

