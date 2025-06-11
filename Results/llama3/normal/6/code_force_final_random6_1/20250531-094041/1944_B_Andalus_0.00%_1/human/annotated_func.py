#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line contains two integers n and k (2 <= n <= 5 * 10^4, 1 <= k <= floor(n/2)). The second line contains 2n integers a_1, a_2, ..., a_{2n} (1 <= a_i <= n). Every integer from 1 to n occurs exactly twice in a. The sum of n over all test cases does not exceed 5 * 10^4.
    T = int(input())
    for _ in range(T):
        n, k = map(int, input().split())
        
        lst = list(map(int, input().split()))
        
        lft = lst[:n]
        
        rgt = lst[n:]
        
        ldb = []
        
        rdb = []
        
        sng = []
        
        lft.sort()
        
        rgt.sort()
        
        for i in range(1, n):
            if lft[i] == lft[i - 1]:
                ldb.append(lft[i])
            elif i < n - 1 and lft[i] != lft[i + 1]:
                sng.append(lft[i])
        
        for i in range(1, n):
            if rgt[i] == rgt[i - 1]:
                rdb.append(rgt[i])
        
        sz = 0
        
        for elem in ldb:
            if sz >= k:
                break
            if k - sz >= 2:
                print(elem, elem, end=' ')
                sz += 2
        
        for elem in sng:
            if sz >= k:
                break
            print(elem, end=' ')
            sz += 1
        
        print()
        
        sz = 0
        
        for elem in rdb:
            if sz >= k:
                break
            if k - sz >= 2:
                print(elem, elem, end=' ')
                sz += 2
        
        for elem in sng:
            if sz >= k:
                break
            print(elem, end=' ')
            sz += 1
        
    #State: Output State: `_` is `T`, `n` is an integer between 2 and 5 * 10^4 inclusive, `k` is an integer between 1 and floor(n/2) inclusive, `lst` is a list of 2n integers between 1 and n inclusive, `lft` is a sorted list of n integers between 1 and n inclusive, `rgt` is a sorted list of n integers between 1 and n inclusive, `ldb` is an empty list, `rdb` is an empty list, `sng` is an empty list, `sz` is equal to `k`, `i` is `n - 1`, `elem` is `None`, and `stdin` contains no test cases.
    #
    #In natural language, the output state after the loop executes all the iterations is that the loop has iterated over all test cases in the input, processing each test case and printing the required output. The loop has finished executing, and all variables have reached their final state. The lists `ldb`, `rdb`, and `sng` are empty, indicating that all elements have been processed. The size `sz` has reached the value `k`, and the index `i` has reached the end of the lists `lft` and `rgt`. The variable `elem` is `None`, indicating that there are no more elements to process. Finally, the input `stdin` is empty, indicating that all test cases have been processed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two lines. The first line contains two integers n and k, and the second line contains 2n integers. The function processes each test case by sorting the integers, identifying pairs and singletons, and printing the first k pairs and singletons. The function iterates over all test cases, processing each one and printing the required output, until all test cases have been processed and the input is empty.

