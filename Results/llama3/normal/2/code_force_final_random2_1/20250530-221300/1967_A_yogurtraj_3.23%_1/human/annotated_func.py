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
        
    #State: ii is equal to the number of test cases, n is 0, a is an empty list, i is -1, stdin is empty, and the values of (r - 1) * n + 1 or (r - 1) * n + 1 + rem + y are printed for each test case.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two lines: the first line contains two integers n and k, and the second line contains n integers. It then processes each test case by sorting the integers, calculating a value r based on the sorted integers and k, and printing a result for each test case. The result is either (r - 1) * n + 1 or (r - 1) * n + 1 + rem + y, depending on the value of k. After processing all test cases, the function leaves the input stream empty and the variables n, a, and i in a final state of 0, empty list, and -1, respectively.

