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
            print((r - 1) * n + 1 + k % n)
        else:
            print((r - 1) * n + 1 + rem + y)
        
    #State: ii is equal to the number of test cases, n is an integer, a is a sorted list of integers equal to the last input, stdin contains 0 test cases. If k is not equal to 0, the value of the expression (a[n - 1] - 1) * n + 1 + k % n is printed, where k is either 0 or reduced by (n - 1) * (a[n - 1] - a[n - 2]). If k is 0, r is a[i] + k // (i + 1), rem is k % (i + 1), and y is n - 1 - i, and this is printed: ((a[i] + k // (i + 1)) - 1) * n + 1 + (k % (i + 1)) + (n - 1 - i)

#Overall this is what the function does:This function processes multiple test cases from standard input, where each test case consists of two lines: the first line contains two integers n and k, and the second line contains n integers. The function sorts the integers, then iterates through them to find the maximum value that can be achieved by adding k to the smallest integer. If k is not exhausted, it adds the remaining value to the last integer. The function prints the calculated value for each test case.

