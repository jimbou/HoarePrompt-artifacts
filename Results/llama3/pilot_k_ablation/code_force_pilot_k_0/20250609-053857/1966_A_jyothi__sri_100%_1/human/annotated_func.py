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
        
    #State: t is 0, and the standard output contains t lines, each with an integer value.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of two integers (n and k) and a list of n integers. It then calculates the minimum number of elements that need to be removed from the list so that no element appears at least k times. The function prints the result for each test case.

