#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 500) followed by t test cases. Each test case consists of two lines. The first line contains two integers n and k (1 <= n <= 100, 2 <= k <= 100). The second line contains n integers c_1, c_2, ..., c_n (1 <= c_i <= 100).
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
        
    #State: stdin is empty, `n` is 0, `k` is 0, `a` is an empty list, `h` is an empty dictionary, `ans` is the last value printed, `_` is the number of test cases, and the value of `ans` has been printed for each test case.

#Overall this is what the function does:This function reads input from stdin, processes multiple test cases, and prints the result for each case. It accepts no parameters and returns no value. The function's purpose is to calculate and print the result for each test case based on the given input. The final state of the program is that stdin is empty, and the results for all test cases have been printed.

