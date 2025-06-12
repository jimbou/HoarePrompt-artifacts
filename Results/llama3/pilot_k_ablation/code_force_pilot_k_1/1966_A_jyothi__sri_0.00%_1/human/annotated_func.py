#State of the program right berfore the function call: stdin contains t test cases. Each test case contains two integers n and k (1 <= n <= 100, 2 <= k <= 100) and n integers c_1, c_2, ..., c_n (1 <= c_i <= 100).
    for _ in range(int(input())):
        n, k = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        h = {}
        
        ans = n
        
        for i in a:
            if i in h:
                h[i] += 1
            else:
                h[i] = 1
            if h[i] >= k:
                ams = k - 1
        
        print(ans)
        
    #State: `stdin` is empty, `t` is 0, `n` is not defined, `k` is not defined, `a` is not defined, `h` is not defined, `ans` is not defined, `_` is `t`

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of two integers n and k, followed by n integers. It then processes each test case by counting the occurrences of each integer and updating a variable 'ans' to n. However, the code has a logical error, as the variable 'ams' is assigned a value but not used anywhere, and the variable 'ans' is not updated correctly based on the count of integers. The function prints the value of 'ans' for each test case, but due to the logical error, the output may not be accurate. The function continues until all test cases are processed, leaving the standard input empty.

