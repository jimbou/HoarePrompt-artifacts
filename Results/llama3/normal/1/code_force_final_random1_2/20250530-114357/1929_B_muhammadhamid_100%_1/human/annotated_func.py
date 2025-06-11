#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains an integer t (1 <= t <= 1000). Each of the following t lines contains two integers n and k (2 <= n <= 10^8, 1 <= k <= 4n - 2).
    for _ in range(int(input())):
        n, k = map(int, input().split())
        
        if k == 1:
            print(1)
            continue
        
        if k <= 2 * (n + (n - 2)):
            print(math.ceil(k / 2))
        else:
            print(k // 2 + 1)
        
    #State: `n` and `k` are integers, `_` is `t`, stdin is empty.

#Overall this is what the function does:This function reads multiple lines of input from stdin, where the first line contains an integer t, and each of the following t lines contains two integers n and k. It then processes each pair of n and k, and prints the result of a calculation based on the values of k and n. The function continues this process until all input lines have been processed, leaving stdin empty.

