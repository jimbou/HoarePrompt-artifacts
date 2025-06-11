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
        
    #State: T is 0, _ is T, n is an integer between 3 and 5 * 10^4 inclusive, k is an integer between 1 and floor(n/2) inclusive, lst is an empty list, lft is a sorted list of n integers between 1 and n inclusive, rgt is a sorted list of n integers between 1 and n inclusive, ldb is an empty list, sng is a list that must have at least 2 times k elements, elem is the last element in the list sng that was printed, rdb is an empty list, sz is 2 times k, stdin is empty, i is equal to n, and a new line is printed for every test case.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two lines. The first line contains two integers n and k, and the second line contains 2n integers. The function then processes these integers, separating them into two lists (lft and rgt), and further categorizes them into three lists: ldb (duplicates from lft), rdb (duplicates from rgt), and sng (single occurrences from lft). It then prints a sequence of integers, prioritizing duplicates from ldb and rdb, followed by single occurrences from sng, until a total of 2k integers are printed. This process is repeated for each test case, and the function concludes by printing a new line for every test case.

