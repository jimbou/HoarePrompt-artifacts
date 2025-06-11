#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line contains two integers n and k (1 <= n <= 2 * 10^5, 0 <= k <= 10^12). The second line contains n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^12).
    for ii in range(int(input())):
        n, k = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        a.sort()
        
        r = a[0]
        
        rem = 0
        
        y = 0
        
        for i in range(0, n - 1):
            if (i + 1) * (a[i + 1] - a[i]) > k:
                r = a[i] + k // (i + 1)
                rem = k % (i + 1)
                y = n - 1 - i
                k = 0
                break
            else:
                k -= (i + 1) * (a[i + 1] - a[i])
                r = a[i + 1]
        
        if k != 0:
            r = a[n - 1] + k // n
            print((r - 1) * n + 1)
        else:
            print((r - 1) * n + 1 + rem + y)
        
    #State: n is an integer greater than or equal to 1, k is an integer, a is a sorted list of integers, r is an integer, rem is an integer, y is an integer, ii is equal to the number of test cases, i is n - 1, stdin is empty. If k is not equal to 0, then the program prints ((a[n - 1] + k // n) - 1) * n + 1. If k is equal to 0, then the program prints (r - 1) * n + 1 + rem + y.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two lines. The first line contains two integers, n and k, and the second line contains n integers. The function sorts the integers, then iterates through them to find a value r based on the value of k. If k is not zero, the function prints a calculated value based on the last integer in the sorted list and k. If k is zero, the function prints a calculated value based on r, the remainder of k divided by the number of integers, and the number of remaining integers. The function repeats this process for each test case, emptying the standard input.

