#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains a single integer t (1 ≤ t ≤ 676). Each of the following t lines contains two integers n (1 ≤ n ≤ 26) and k (1 ≤ k ≤ 26).
    t = int(input())
    for i in range(t):
        n, k = map(int, input().split())
        
        print('abcdefghijklmnopqrstuvwxyz'[:k] * n)
        
    #State: The output will be a series of strings, each consisting of the first k letters of the alphabet repeated n times. The number of strings will be equal to the value of t. The value of t will be unchanged, as it is not modified within the loop. The input from stdin will be consumed by the loop, so stdin will be empty after the loop finishes executing.

#Overall this is what the function does:The function reads a series of input lines from stdin, where the first line contains an integer t, and each subsequent line contains two integers n and k. It then generates and prints t strings, each consisting of the first k letters of the alphabet repeated n times. The function consumes all input from stdin and leaves it empty. The output is a series of strings, with the number of strings equal to the value of t.

