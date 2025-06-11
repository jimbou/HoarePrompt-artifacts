#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line contains two integers n and k (2 <= n <= 5 * 10^4, 1 <= k <= floor(n/2)). The second line contains 2n integers a_1, a_2, ..., a_{2n} (1 <= a_i <= n). Every integer from 1 to n occurs exactly twice in a. The sum of n over all test cases does not exceed 5 * 10^4.
    t = int(input())
    for q in range(t):
        n, k = list(map(int, input().split(' ')))
        
        a = list(map(int, input().split(' ')))
        
        b = a[:n]
        
        c = a[n:]
        
        b.sort()
        
        c.sort()
        
        ans1 = []
        
        ans2 = []
        
        k = 2 * k
        
        req = k
        
        l = []
        
        for i in range(1, n):
            if k == 0:
                break
            if b[i] == b[i - 1]:
                ans1.append(b[i])
                ans1.append(b[i])
                k -= 2
            elif b[i - 1] not in ans1:
                l.append(b[i - 1])
        
        if b[n - 1] not in ans1:
            l.append(b[n - 1])
        
        k = req
        
        for i in range(1, n):
            if k == 0:
                break
            if c[i] == c[i - 1]:
                ans2.append(c[i])
                ans2.append(c[i])
                k -= 2
        
        for i in range(len(l)):
            if k == 0:
                break
            ans1.append(l[i])
            ans2.append(l[i])
        
        print(*ans1)
        
        print(*ans2)
        
    #State: The output state will be a series of pairs of arrays, where each pair represents the result of a test case. The first array in each pair contains the elements from the first half of the input array that are either duplicates or have been added from the left-over list, and the second array contains the elements from the second half of the input array that are duplicates. The arrays are sorted in ascending order. The number of pairs is equal to the number of test cases (t).

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two lines. The first line contains two integers n and k, and the second line contains 2n integers. The function then processes these integers, separating them into two halves, sorting each half, and identifying duplicates. It constructs two arrays, one from the first half and one from the second half, by prioritizing duplicates and then adding non-duplicate elements from the first half if necessary. The function prints these two arrays in ascending order for each test case. The output consists of a series of pairs of arrays, where each pair represents the result of a test case.

