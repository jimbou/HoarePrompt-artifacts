#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of two lines. The first line contains two integers n and k (1 <= n <= 2 * 10^5, 0 <= k <= 10^12). The second line contains n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^12).
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
        
    #State: ii is equal to the number of test cases, stdin is empty, n is an integer, k is an integer, i is n - 1, a is a sorted list of integers, r is an integer, rem is an integer, and y is an integer. If k is not equal to 0, the value of the expression `(r - 1) * n + 1 + k % n` which is equal to `(a[n - 1] + k // n - 1) * n + 1 + k % n` is printed. If k is 0, the value of the expression `(r - 1) * n + 1 + rem + y` is printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two lines. The first line contains two integers n and k, and the second line contains n integers. The function sorts the integers, calculates a value r based on the sorted integers and k, and prints a value calculated from r, n, and k. The function repeats this process for each test case until standard input is empty.

