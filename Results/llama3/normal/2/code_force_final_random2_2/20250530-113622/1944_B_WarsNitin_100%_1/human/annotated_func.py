#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line contains two integers n and k (2 <= n <= 5 * 10^4, 1 <= k <= floor(n/2)). The second line contains 2n integers a_1, a_2, ..., a_2n (1 <= a_i <= n). Every integer from 1 to n occurs exactly twice in a. The sum of n over all test cases does not exceed 5 * 10^4.
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
        
        if b[0] != b[1]:
            l.append(b[0])
        
        if b[n - 2] != b[n - 1]:
            l.append(b[n - 1])
        else:
            ans1.append(b[n - 1])
            ans1.append(b[n - 1])
            k -= 2
        
        for i in range(1, n - 1):
            if k == 0:
                break
            if b[i] == b[i - 1]:
                ans1.append(b[i])
                ans1.append(b[i])
                k -= 2
            elif b[i] != b[i + 1]:
                l.append(b[i])
        
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
            k -= 1
        
        print(*ans1)
        
        print(*ans2)
        
    #State: t is 0, q is t, stdin contains no test cases, n is an integer between 2 and 5 * 10^4 inclusive, a is a list of 2n integers between 1 and n inclusive, b is a sorted list of n integers between 1 and n inclusive, c is a sorted list of n integers between 1 and n inclusive, ans1 is a list containing two times the value of b[i] for all i where b[i] is equal to b[i - 1] and l[i], ans2 is either an empty list or a list containing two times the value of c[i] if c[i] is equal to c[i - 1] and l[i], req is an integer equal to 0, i is n, l is either a list containing the first element of b, the last element of b and b[i] for all i where b[i] is not equal to b[i + 1] or an empty list depending on the second last element of b that must have at least n elements, and k is either -n or a value greater than -n, and the list ans1 is printed, and the list ans2 is printed

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two lines. The first line contains two integers n and k, and the second line contains 2n integers. The function then processes these integers, sorting them and creating two lists, ans1 and ans2, based on certain conditions. It prints the contents of ans1 and ans2. The function repeats this process for all test cases, ultimately consuming all input from standard input.

