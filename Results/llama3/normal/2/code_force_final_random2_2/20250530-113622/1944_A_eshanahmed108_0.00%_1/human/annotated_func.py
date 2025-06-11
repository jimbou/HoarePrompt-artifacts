#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^3) followed by t lines, each containing two integers n and k (1 <= n <= 100, 0 <= k <= n*(n-1)/2).
    for _ in range(int(input())):
        n, k = map(int, input().split())
        
        print(n if n - k <= 1 else 1)
        
    #State: the value of `n` if the difference between `n` and `k` is less than or equal to 1, otherwise 1, is printed t times.

#Overall this is what the function does:Prints the value of `n` if the difference between `n` and `k` is less than or equal to 1, otherwise prints 1, for each of `t` test cases.

