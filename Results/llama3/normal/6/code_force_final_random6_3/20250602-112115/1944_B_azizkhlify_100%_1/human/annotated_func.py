#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line contains two integers n and k (2 <= n <= 5 * 10^4, 1 <= k <= floor(n/2)). The second line contains 2n integers a_1, a_2, ..., a_2n (1 <= a_i <= n). Every integer from 1 to n occurs exactly twice in a. The sum of n over all test cases does not exceed 5 * 10^4.
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
        
    #State: ul and ur are equal, and the loop has printed all elements in the list `res` separated by a space and has terminated.

#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of two lines. The first line contains two integers n and k, and the second line contains 2n integers. The function then processes these integers, printing pairs of identical integers until it reaches a count of k pairs, and then prints a sequence of unique integers until it reaches a count of k. Finally, it prints the same sequence of unique integers again, ensuring that the total count of printed integers is equal on both sides. The function repeats this process for all test cases and terminates.

