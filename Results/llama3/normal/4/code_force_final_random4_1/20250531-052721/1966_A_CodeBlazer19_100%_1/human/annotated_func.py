#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 500) followed by t test cases. Each test case consists of two lines. The first line contains two integers n and k (1 <= n <= 100, 2 <= k <= 100). The second line contains n integers c_1, c_2, ..., c_n (1 <= c_i <= 100).
    t = int(input())
    for i in range(t):
        n, k = map(int, input().split())
        
        l = list(map(int, input().split()))
        
        p = [l.count(j) for j in set(l)]
        
        if max(p) >= k:
            print(k - 1)
        else:
            print(n)
        
    #State: t is an integer between 1 and 500 inclusive, i is t-1, stdin is empty, n is an integer between 1 and 100, k is an integer between 2 and 100, l is a list of n integers between 1 and 100, p is a list of counts of each unique integer in l. If the maximum count of any unique integer in l is greater than or equal to k, then k-1 is printed. Otherwise, the value of n is printed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of two lines: the first line contains two integers n and k, and the second line contains n integers. The function then determines the maximum count of any unique integer in the list of n integers. If this maximum count is greater than or equal to k, it prints k-1; otherwise, it prints the value of n. The function repeats this process for each test case, and once all test cases have been processed, it leaves the standard input empty.

