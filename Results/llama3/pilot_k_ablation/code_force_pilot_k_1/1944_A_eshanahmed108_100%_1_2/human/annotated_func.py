#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^3) followed by t lines, each containing two integers n and k (1 <= n <= 100, 0 <= k <= n*(n-1)/2).
    for _ in range(int(input())):
        n, k = map(int, input().split())
        
        print(n if n - k > 1 else 1)
        
    #State: stdin is empty, and the program has printed t lines, each containing either the value of `n` if `n - k` was greater than 1 for that iteration, or 1 if `n - k` was not greater than 1.

#Overall this is what the function does:The function reads a series of test cases from standard input, where each case consists of two integers n and k. It then prints the value of n if n is greater than k + 1, otherwise it prints 1. This process is repeated for each test case, resulting in a series of printed values equal to the number of test cases.

