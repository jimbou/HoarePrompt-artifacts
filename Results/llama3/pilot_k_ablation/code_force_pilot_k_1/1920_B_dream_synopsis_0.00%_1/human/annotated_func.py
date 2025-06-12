#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of two lines. The first line contains three integers n, k, and x (1 <= n <= 2 * 10^5, 1 <= x, k <= n). The second line contains n integers a_1, a_2, ..., a_n (1 <= a_i <= 1000). The number of test cases is given by an integer t (1 <= t <= 10^4) in the first line of the input.
    for _ in range(int(input())):
        n, k, x = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        a.sort()
        
        a.reverse()
        
        sum1 = sum(a)
        
        ans = []
        
        for i in range(k + 1):
            if i == 0:
                sums = sum1 - 2 * sum(a[:x + 1])
                ans.append(sums)
            elif i + x - 1 < n:
                sums = sums + a[i - 1] - 2 * a[i + x - 1]
                ans.append(sums)
            else:
                sums = sums + a[i - 1]
                ans.append(sums)
        
        print(max(ans))
        
    #State: `stdin` is empty, `n`, `k`, `x`, `a`, `sum1`, `ans`, and `_` are undefined, and all test cases have been processed and their maximum values printed.

#Overall this is what the function does:This function processes multiple test cases from standard input, where each test case consists of two lines: the first line contains three integers n, k, and x, and the second line contains n integers. The function sorts the integers in descending order, calculates a series of sums by subtracting pairs of integers from the total sum, and prints the maximum sum for each test case. After processing all test cases, the function leaves the standard input empty and all variables undefined.

