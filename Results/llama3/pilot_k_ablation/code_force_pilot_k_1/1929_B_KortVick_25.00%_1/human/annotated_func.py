#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t lines, each containing two integers n and k (2 <= n <= 10^8, 1 <= k <= 4n - 2).
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        
        if k % 2 == 0 and k // 2 % 2 == 1:
            print(k // 2 + 1)
        else:
            print(ceil(k / 2))
        
    #State: `t` is 0, stdin is empty.

#Overall this is what the function does:Reads a series of test cases from standard input, where each case consists of two integers n and k, and for each case, prints the smallest integer greater than or equal to k/2.

