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
        
    #State: T is equal to 0, _ is equal to T, stdin contains no test cases, n is an integer between 2 and 5 * 10^4 inclusive, lst is a list of 2n integers between 1 and n inclusive, lft is a sorted list of n integers between 1 and n inclusive, rgt is a sorted list of n integers between 1 and n inclusive, ldb is a list containing all the values of lft that are equal to the previous value, rdb is a list containing all the values of rgt that are equal to the previous value, sng is a list containing all the values of lft that are not equal to the previous value and the next value, elem is the last element in the list sng, i is equal to n, and sz is equal to k.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two lines. The first line contains two integers n and k, and the second line contains 2n integers. The function then processes these integers, separating them into two sorted lists (lft and rgt) and identifying duplicate and single elements in each list. It prints out a sequence of integers, prioritizing duplicates from both lists and then singles from the first list, until it reaches a total count of k. This process is repeated for each test case.

