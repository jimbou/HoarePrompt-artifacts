#State of the program right berfore the function call: stdin contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 100). Each test case consists of two lines. The first line contains two integers n and k (1 ≤ n ≤ 2 * 10^5, 0 ≤ k ≤ 10^12). The second line contains n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^12).
    for _ in range(int(input())):
        n, k = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        m = min(a)
        
        ans = 0
        
        if k >= n * m:
            ans = math.factorial(n)
        else:
            k -= n * m
            for i in range(n):
                a[i] = m + min(k, m + k // n - a[i])
                k -= min(k, m + k // n - a[i])
            ans = a[0]
            for i in range(1, n):
                ans *= a[i] - a[i - 1]
        
        print(ans)
        
    #State: n is an integer equal to 0, k is an integer equal to 0, a is an empty list, m is an integer equal to 0, ans is an integer equal to 1, _ is equal to the number of test cases, i is an integer equal to 0, stdin contains no inputs, and the value of ans is printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two lines. The first line contains two integers n and k, and the second line contains n integers a_1 to a_n. For each test case, it calculates the minimum value m in the list a, and then determines the value of ans based on the condition k >= n * m. If true, ans is set to the factorial of n; otherwise, it adjusts the values in list a and calculates ans as the product of the differences between consecutive elements in the adjusted list. Finally, it prints the value of ans for each test case.

