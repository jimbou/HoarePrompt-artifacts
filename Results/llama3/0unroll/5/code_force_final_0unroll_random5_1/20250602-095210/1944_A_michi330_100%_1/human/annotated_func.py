#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^3) followed by t lines, each containing two integers n and k (1 <= n <= 100, 0 <= k <= n*(n-1)/2).
    t = int(input())
    for i in range(0, t, 1):
        n, k = map(int, input().split())
        
        if k >= n - 1:
            print(1)
        else:
            print(n)
        
    #State: The loop will print either 1 or n for each of the t input lines. If k is greater than or equal to n-1, it will print 1; otherwise, it will print n. The value of t remains unchanged.

#Overall this is what the function does:The function reads an integer t from standard input, representing the number of test cases, and then for each test case, it reads two integers n and k. It prints 1 if k is greater than or equal to n-1, otherwise it prints n. The function does not modify the input values and does not return any value, only printing the results for each test case.

