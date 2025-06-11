#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two integers n and k such that 2 <= n <= 10^8 and 1 <= k <= 4n - 2.
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        
        if k % 2 == 0 and k // 2 % 2 == 1:
            print(k // 2 + 1)
        else:
            print(ceil(k / 2))
        
    #State: `_` is equal to `t`, stdin is empty.

#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of two integers n and k. It then calculates and prints the result for each test case based on the parity of k and k/2. The function consumes all input from standard input and produces a result for each test case, leaving standard input empty.

