#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line contains two integers n and k (1 <= n <= 2 * 10^5, 0 <= k <= 10^12). The second line contains n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^12).
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
        
    #State: The output state is a series of integers, each representing the number of ways to arrange the elements of the array a in non-decreasing order, given the constraints of the problem. The number of integers in the output state is equal to the number of test cases in the input state.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two lines. The first line contains two integers n and k, and the second line contains n integers. The function calculates the number of ways to arrange the elements of the array in non-decreasing order, given the constraint that the sum of the elements does not exceed k. It prints the result for each test case.

