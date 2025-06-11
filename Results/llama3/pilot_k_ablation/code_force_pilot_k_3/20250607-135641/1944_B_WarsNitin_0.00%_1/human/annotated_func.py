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
        
    #State: t is a positive integer, q is equal to t, n is an integer, b is a sorted list of n integers, c is a sorted list of integers, req is an even integer equal to twice the original value of k, k is 0, stdin is empty, i is -1, a is a list of integers, ans1 is a list containing all the repeated elements in b and all the elements in l, ans2 is a list containing two occurrences of the current value of c[i] if c[i] is not equal to c[i - 1], otherwise ans2 is a list containing four occurrences of the current value of c[i] and all the elements in l, l is an empty list, and the list of all the repeated elements in b and all the elements in l is being printed, and this is printed: two occurrences of the current value of c[i] if c[i] is not equal to c[i - 1], otherwise four occurrences of the current value of c[i] and all the elements in l

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two lines. The first line contains two integers n and k, and the second line contains 2n integers. The function then processes these integers, sorting them and selecting specific elements based on the value of k. It prints two lists of integers for each test case, where the first list contains all repeated elements from the first half of the input integers and some additional elements, and the second list contains two occurrences of each element from the second half of the input integers, with some elements repeated four times. The function continues this process until all test cases have been processed, at which point the standard input is empty.

