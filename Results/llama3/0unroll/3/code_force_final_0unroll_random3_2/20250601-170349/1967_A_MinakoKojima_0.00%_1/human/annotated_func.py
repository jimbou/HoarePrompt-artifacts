#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line contains two integers n and k, where n is a positive integer and k is a non-negative integer. The second line contains n non-negative integers.
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
        
    #State: The output state after the loop executes all the iterations is a list of integers, where each integer is the result of the calculation for each test case. The result for each test case is either the factorial of n if k is greater than or equal to n times the minimum value in the list a, or the product of the differences between consecutive elements in the list a after adjusting the values in a based on k and the minimum value in a.

#Overall this is what the function does:Calculates and prints the result of a series of test cases, where each test case involves adjusting a list of non-negative integers based on a given minimum value and a non-negative integer k, and then computing the product of the differences between consecutive elements in the adjusted list, or the factorial of the list length if k is greater than or equal to the product of the list length and the minimum value.

