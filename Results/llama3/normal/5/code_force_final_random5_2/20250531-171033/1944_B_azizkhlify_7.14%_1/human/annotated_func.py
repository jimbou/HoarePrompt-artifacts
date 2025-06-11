#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line contains two integers n and k (2 <= n <= 5 * 10^4, 1 <= k <= floor(n/2)). The second line contains 2n integers a_1, a_2, ..., a_{2n} (1 <= a_i <= n). Every integer from 1 to n occurs exactly twice in a. The sum of n over all test cases does not exceed 5 * 10^4.
    for _ in range(int(input())):
        n, k = [int(i) for i in input().split()]
        
        a = [int(i) for i in input().split()]
        
        l = [0] * n
        
        r = [0] * n
        
        re = ul = ur = 0
        
        res = []
        
        for i in range(n):
            l[a[i] - 1] += 1
        
        for i in range(n, 2 * n):
            r[a[i] - 1] += 1
        
        for i in range(n):
            if l[a[i] - 1] == 2:
                print(a[i], a[i], end=' ')
                ul += 2
            if ul == k * 2:
                break
        
        k = 2 * k - ul
        
        if k:
            for i in range(n):
                if l[a[i] - 1] == 1:
                    print(a[i], end=' ')
                    re += 1
                    res.append(a[i])
                if re == k:
                    break
        
        print()
        
        for i in res:
            print(i, end=' ')
        
        if ul != ur:
            for i in range(n, 2 * n):
                if r[a[i] - 1] == 2:
                    print(a[i], a[i], end=' ')
                    ur += 2
                if ul == ur:
                    break
        
        print()
        
    #State: n is a positive integer greater than 0, k is 0, a is a list of n integers, l is a list of n integers where the value at index a[i] - 1 is either 2 or 0, r is a list of n integers where the value at index a[i] - 1 is n and all other values are 1, re is either 0 or 1 or 2 or ... or n, ul is either 0 or 2 or 4 or 6 or ... or 2n, ur is either 0 or 2 or 4 or 6 or ... or 2n, res is a list containing all values of a[i], and all elements in the list res have been printed, i is 2n. If ul is not equal to ur, then i is 2n. If ul is equal to ur, then we break out of the most internal loop or if statement. Otherwise, no action is taken, and nothing is printed.

#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of two lines. The first line contains two integers n and k, and the second line contains 2n integers. The function then processes the input data, printing pairs of identical integers from the first half of the input list, followed by single integers from the first half that have not been printed yet, and finally printing pairs of identical integers from the second half of the input list if necessary. The function repeats this process for each test case.

