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
        
    #State: ii is equal to the number of test cases, n is an integer, a is a sorted list of integers, r is an integer, rem is an integer, y is an integer, stdin is empty. If k is not 0, the value of the expression (r - 1) * n + 1 + k % n is printed, where r is a[n - 1] + k // n. If k is 0, the value of the expression (r - 1) * n + 1 + rem + y is printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two lines. The first line contains two integers n and k, and the second line contains n integers. The function sorts the integers, calculates a value r based on the sorted integers and k, and then prints a value calculated from r, n, and either k or the remainder of k divided by n, depending on whether k is 0 or not. The function repeats this process for each test case, emptying the standard input in the process.

