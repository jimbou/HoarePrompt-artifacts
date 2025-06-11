#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains a single integer t (1 ≤ t ≤ 676). Each of the following t lines contains two integers n (1 ≤ n ≤ 26) and k (1 ≤ k ≤ 26).
    t = int(input())
    for i in range(t):
        n, k = map(int, input().split())
        
        print('abcdefghijklmnopqrstuvwxyz'[:k] * n)
        
    #State: Output State: `t` is an integer equal to 0, stdin contains 0 lines of input.

#Overall this is what the function does:This function reads a specified number of lines from standard input, where each line contains two integers, and prints a repeated sequence of letters from 'a' to 'z' based on the second integer, repeated a number of times equal to the first integer. The function consumes all input lines and produces output for each pair of integers read.

