#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: two integers n and k, where n is a positive integer less than or equal to 100 and k is a non-negative integer less than or equal to n*(n-1)/2.
    t = int(input())
    for i in range(0, t, 1):
        n, k = map(int, input().split())
        
        if k >= n - 1:
            print(1)
        else:
            print(n - 1)
        
    #State: `t` is greater than or equal to 0, `i` is equal to `t`, `n` is a positive integer, `k` is a non-negative integer less than or equal to `n*(n-1)/2`, stdin contains no input. If `k` is greater than or equal to `n - 1`, then 1 is printed. Otherwise, the value of `n-1` is printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two integers n and k. It then prints the minimum number of operations required to make all pairs of elements in a set of n elements distinct, given that k pairs are already distinct. If k is greater than or equal to n-1, it prints 1; otherwise, it prints n-1. The function processes all test cases and then terminates, leaving the standard input empty.

