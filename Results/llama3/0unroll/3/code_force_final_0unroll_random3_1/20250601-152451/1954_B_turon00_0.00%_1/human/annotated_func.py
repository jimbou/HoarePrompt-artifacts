#State of the program right berfore the function call: stdin contains t test cases. Each test case contains two inputs: first an integer n, then a list of n integers.
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = list(map(int, input().strip().split()))
        
        tmp = a[0]
        
        aa = set(a)
        
        if len(aa) == 1:
            print(-1)
        
        cnt = 0
        
        ans = n
        
        for i in range(n):
            if a[i] == tmp:
                cnt += 1
            else:
                ans = min(ans, cnt)
                cnt = 0
        
        ans = min(ans, cnt)
        
        print(ans)
        
    #State: The loop will print the minimum number of consecutive occurrences of the first element in each test case, or -1 if all elements are the same. The value of t will be unchanged, and stdin will be empty after all test cases have been processed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer n followed by a list of n integers. It then calculates and prints the minimum number of consecutive occurrences of the first element in each list, or -1 if all elements in the list are the same. After processing all test cases, the function leaves the input stream empty.

