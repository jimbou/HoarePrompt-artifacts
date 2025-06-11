#State of the program right berfore the function call: stdin contains multiple test cases. The first line of stdin contains a single integer t (1 <= t <= 5000) — the number of test cases. For each test case, the first line contains 2 integers n and k (2 <= n <= 5 * 10^4, 1 <= k <= floor(n/2)). The second line contains 2n integers a_1, a_2, ..., a_{2n} (1 <= a_i <= n). Every integer from 1 to n occurs exactly twice in a. The sum of n over all test cases does not exceed 5 * 10^4.
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
                l[a[i] - 1] = 0
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
                    r[a[i] - 1] = 0
                    ur += 2
                if ul == ur:
                    break
        
        print()
        
    #State: The output state is a series of pairs of numbers, where each pair consists of two identical numbers, followed by a series of single numbers. The pairs are formed by selecting numbers that appear twice in the first half of the input list, and the single numbers are formed by selecting numbers that appear only once in the first half of the input list. The number of pairs is determined by the value of k, and the number of single numbers is determined by the remaining value of k after forming the pairs. The output is repeated for each test case.

#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of two lines. The first line contains two integers, n and k, and the second line contains 2n integers. The function then processes the input data to form pairs of identical numbers and single numbers based on their occurrence in the first half of the input list. The number of pairs is determined by the value of k, and the remaining value of k is used to determine the number of single numbers. The function prints the pairs and single numbers for each test case, with the pairs consisting of two identical numbers and the single numbers being the remaining numbers that appear only once in the first half of the input list.

