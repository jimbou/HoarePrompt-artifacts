#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 500) followed by t test cases. Each test case consists of two lines. The first line contains two integers n and k (1 <= n <= 100, 2 <= k <= 100). The second line contains n integers c_1, c_2, ..., c_n (1 <= c_i <= 100).
    t = int(input())
    while t > 0:
        n, k = map(int, input().split())
        
        arrC = list(map(int, input().split()))
        
        hashmap = {}
        
        ans = n
        
        for i in arrC:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
            if hashmap[i] >= k:
                ans = k - 1
        
        print(ans)
        
        t -= 1
        
    #State: t is 0, n is an integer between 1 and 100 inclusive, k is an integer between 2 and 100 inclusive, arrC is an empty list, hashmap is a dictionary containing all integers from the original list with their respective counts, ans is either n or k - 1, and ans which is either n or k - 1 is being printed.

#Overall this is what the function does:The function reads a series of test cases from standard input, where each test case consists of two lines: the first line contains two integers n and k, and the second line contains n integers. It then counts the occurrences of each integer and determines the minimum between n and k-1, printing this value for each test case. The function continues this process until all test cases have been processed, at which point it terminates.

