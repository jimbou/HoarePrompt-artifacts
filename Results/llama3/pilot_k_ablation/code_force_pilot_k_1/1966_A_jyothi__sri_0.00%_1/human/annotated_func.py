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
        
    #State: t is 0, stdin is empty, _ is equal to the initial value of t, n and k are the values of the last test case, a is the list of the last test case, h is a dictionary where keys are elements of a and values are their frequencies, ans is equal to the minimum of n and k - 1 for the last test case, and the minimum of n and k - 1 for each test case has been printed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of two lines: the first line contains two integers n and k, and the second line contains n integers. For each test case, it calculates the minimum of n and k-1, and prints this value. The function does not return any value, but rather prints the results for each test case. After processing all test cases, the function leaves the input stream empty and the variables n, k, and ans with the values from the last test case.

