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
        
    #State: t is 0, stdin is empty, n is an integer between 1 and 100 (inclusive), k is an integer between 2 and 100 (inclusive), arrC is a list of integers that must have at least n elements, hashmap is a dictionary where each key is an element in arrC and its corresponding value is the frequency of that element in arrC, i is the last element in arrC, and ans is either n or k-1 (where ans is k-1 if any element in arrC has a frequency greater than or equal to k, otherwise ans is n), and ans is printed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of two lines: the first line contains two integers n and k, and the second line contains n integers. It then counts the frequency of each integer in the second line and determines the minimum value between n and k-1, where k-1 is only considered if any integer appears at least k times. The function prints this minimum value for each test case.

