#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line contains two integers n and k (2 <= n <= 5 * 10^4, 1 <= k <= floor(n/2)). The second line contains 2n integers a_1, a_2, ..., a_2n (1 <= a_i <= n). Every integer from 1 to n occurs exactly twice in a. The sum of n over all test cases does not exceed 5 * 10^4.
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
        
        if lft[0] != lft[1]:
            sng.append(lft[0])
        
        for i in range(1, n):
            if lft[i] == lft[i - 1]:
                ldb.append(lft[i])
            elif i == n - 1 or lft[i] != lft[i + 1]:
                sng.append(lft[i])
        
        for i in range(1, n):
            if rgt[i] == rgt[i - 1]:
                rdb.append(rgt[i])
        
        sz = 0
        
        for elem in ldb:
            if 2 * k - sz >= 2:
                print(elem, elem, end=' ')
                sz += 2
            else:
                break
        
        for elem in sng:
            if sz >= 2 * k:
                break
            print(elem, end=' ')
            sz += 1
        
        print()
        
        sz = 0
        
        for elem in rdb:
            if 2 * k - sz >= 2:
                print(elem, elem, end=' ')
                sz += 2
            else:
                break
        
        for elem in sng:
            if sz >= 2 * k:
                break
            print(elem, end=' ')
            sz += 1
        
        print()
        
    #State: `T` is 0, `_` is `T`, `n` is undefined, `k` is undefined, `lst` is undefined, `lft` is undefined, `rgt` is undefined, `ldb` is undefined, `sng` is undefined, `rdb` is undefined, `sz` is undefined.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two lines. The first line contains two integers n and k, and the second line contains 2n integers. The function then processes these integers, separating them into two lists (left and right), and further categorizes them into three groups: left doubles, right doubles, and singles. It then prints out a subset of these integers, prioritizing doubles and then singles, until it reaches a total count of 2k for each test case. The function repeats this process for all test cases.

