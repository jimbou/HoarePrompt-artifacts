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
        
    #State: n is greater than or equal to 0, k is 0, a is a list of n integers, l is a list of n integers where l[a[i] - 1] is 2 for all i in range(n), r is a list of n integers where r[a[i] - 1] is 2 for all i in range(n), re is 0, ul is 2 * n, ur is 2 * n, res is an empty list, and i is equal to 2 * n.

#Overall this is what the function does:The function processes multiple test cases from standard input, where each test case consists of two lines. The first line contains two integers n and k, and the second line contains 2n integers. The function then performs the following actions:

- It counts the occurrences of each integer in the first and second halves of the input list.
- It prints pairs of identical integers from the first half of the list until it reaches the target count k.
- If k is not fully satisfied, it prints a single integer from the first half of the list to partially satisfy k.
- It prints the same single integer again.
- If there are remaining pairs of identical integers in the second half of the list, it prints them until the counts from both halves are equal.

The function repeats this process for all test cases in the input.

