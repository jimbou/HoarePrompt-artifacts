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
        
    #State: The output state after the loop executes all the iterations is a series of lines, each containing a sequence of integers. The sequence is constructed by first printing pairs of identical integers from the first half of the input sequence, then printing a single integer from the first half of the input sequence, and finally printing pairs of identical integers from the second half of the input sequence. The number of pairs and single integers printed is determined by the values of n and k.

#Overall this is what the function does:The function processes multiple test cases from standard input, where each test case consists of two lines. The first line contains two integers n and k, and the second line contains 2n integers. The function prints a sequence of integers for each test case, constructed by printing pairs of identical integers from the first half of the input sequence, then a single integer from the first half, and finally pairs of identical integers from the second half. The number of pairs and single integers printed is determined by the values of n and k. The function repeats this process for all test cases in the input.

