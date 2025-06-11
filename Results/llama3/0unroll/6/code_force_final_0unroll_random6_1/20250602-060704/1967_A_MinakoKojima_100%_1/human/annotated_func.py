#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line contains two integers n and k (1 <= n <= 2 * 10^5, 0 <= k <= 10^12). The second line contains n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^12).
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
        
    #State: Output State: `ans_list` is a list containing the results of all test cases. Each result is the maximum possible sum of the elements in the corresponding test case, after applying the given operations. The stdin is empty, as all test cases have been read and processed.
    for a in ans_list:
        print(a)
        
    #State: Output State: The output state is the same as the initial state, with the only difference being that the results of all test cases have been printed to the console. The `ans_list` variable remains unchanged, still containing the maximum possible sum of the elements in each test case.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two lines: the first line contains two integers n and k, and the second line contains n integers. The function processes each test case by sorting the integers, then iteratively applying a series of operations to maximize the sum of the elements. The operations involve adding differences between consecutive elements to the sum, subject to a limit k. The function returns a list of maximum possible sums for each test case, which are then printed to the console.

