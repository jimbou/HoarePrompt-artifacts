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
        
    #State: The output state after the loop executes all the iterations is a series of pairs of integers, where each pair contains two identical integers. The number of pairs is equal to k, and the integers in each pair are selected from the input list in a way that maximizes the number of pairs. The remaining integers that are not part of any pair are printed separately. This process is repeated for each test case in the input.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two lines. The first line contains two integers n and k, and the second line contains 2n integers. The function processes each test case by splitting the integers into two lists, sorting them, and then printing out pairs of identical integers from the lists, maximizing the number of pairs equal to k. If there are remaining integers that are not part of any pair, they are printed separately. This process is repeated for each test case, resulting in a series of pairs of integers and potentially some single integers.

