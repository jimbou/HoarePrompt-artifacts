#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of two lines. The first line contains two integers n and k (1 <= n <= 2 * 10^5, 0 <= k <= 10^12). The second line contains n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^12).
    ans_list = []
    for _ in range(int(input())):
        n, k = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        a.sort()
        
        ans = a[0]
        
        res = n - 1
        
        for i in range(n - 1):
            dif = a[i + 1] - a[i]
            if dif == 0:
                res -= 1
            if dif != 0:
                if k >= dif * (i + 1):
                    ans += dif
                    k -= dif * (i + 1)
                    res -= 1
                else:
                    ans += k // (i + 1)
                    if i != 0:
                        res += k % (i + 1)
                    k = 0
                    break
                if k == 0:
                    break
        
        if k != 0:
            ans += k // n
            res += k % n
        
        ans += (ans - 1) * (n - 1)
        
        ans += res
        
        ans_list.append(ans)
        
    #State: Output State: `ans_list` is a list of integers, where each integer is the result of the loop's execution for each test case. The value of `ans_list` is determined by the input values of `n`, `k`, and the list of integers `a` for each test case.
    for a in ans_list:
        print(a)
        
    #State: Output State: The output state after the loop executes all the iterations is that the values of `ans_list` are printed to the console, one value per line. The values of `n`, `k`, and the list of integers `a` remain unchanged.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two lines: the first line contains two integers n and k, and the second line contains n integers. For each test case, it sorts the integers, calculates a result based on the sorted integers and the value of k, and appends this result to a list. After processing all test cases, it prints each result in the list to the console, one value per line. The function does not modify the input values.

