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
        
    #State: The output state after the loop executes all the iterations is a series of lines, each containing k integers. The integers in each line are pairs of identical numbers from the left half of the input list, followed by single numbers from the left half that do not have a pair, followed by pairs of identical numbers from the right half of the input list, and finally single numbers from the right half that do not have a pair. The numbers are printed in ascending order within each half. The number of lines is equal to the number of test cases T.

#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of two lines. The first line contains two integers n and k, and the second line contains 2n integers. The function processes each test case by splitting the integers into two halves, sorting them, and identifying pairs of identical numbers and single numbers in each half. It then prints k integers for each test case, consisting of pairs of identical numbers from the left half, followed by single numbers from the left half, then pairs of identical numbers from the right half, and finally single numbers from the right half, all in ascending order within each half. The function repeats this process for all test cases, producing a series of lines as output.

