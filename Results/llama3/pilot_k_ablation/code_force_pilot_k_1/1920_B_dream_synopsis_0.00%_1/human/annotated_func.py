#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of two lines. The first line contains three integers n, k, and x (1 <= n <= 2 * 10^5, 1 <= x, k <= n). The second line contains n integers a_1, a_2, ..., a_n (1 <= a_i <= 1000).
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
        
    #State: `stdin` is empty, `n`, `k`, and `x` are positive integers, `a` is a list of integers sorted in descending order, `sum1` is a positive integer, `ans` is a list of integers, and `_` is the number of test cases. The value of `ans` is a list containing `k+1` elements, where each element is the updated value of `sums` after each iteration of the loop, and the maximum value in the list `ans` has been printed for each test case. If there are no test cases, `n`, `k`, `x`, `a`, `sum1`, and `ans` are not defined.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two lines. The first line contains three integers n, k, and x, and the second line contains n integers. The function sorts the integers in descending order, calculates a series of sums by subtracting multiples of the xth largest integer from the total sum, and prints the maximum sum for each test case. If there are no test cases, the function does not perform any actions.

