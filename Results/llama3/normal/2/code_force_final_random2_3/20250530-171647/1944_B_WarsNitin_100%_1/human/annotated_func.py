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
        
    #State: t is an integer greater than or equal to 0, q is t, stdin contains no test cases, n is an integer greater than or equal to 3, a is a list of integers, b is a sorted list of the first n integers from a, c is a sorted list of the remaining integers from a, req is 2k, i is len(l) - 1, k is either -len(l) or non-zero minus len(l) + 1, ans1 is a list containing two copies of the largest integer from b and all elements of l, ans2 is a list containing two copies of each pair of equal consecutive elements from c and all elements of l, and l is either a list containing the smallest integer from b and the largest integer from b, a list containing the largest integer from b, a list containing the smallest integer from b and the ith element of b, and two copies of the nth integer from a and either two copies of the smallest integer from a and the nth integer from a, two copies of the nth integer from a, or two copies of the smallest integer from a and the ith element of b are printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two lines. The first line contains two integers n and k, and the second line contains 2n integers. The function then processes these integers, sorting them and selecting specific elements based on certain conditions. It prints two lists of integers, ans1 and ans2, which contain specific elements from the input, including pairs of equal consecutive elements and single elements that meet certain criteria. The function repeats this process for each test case, ultimately printing the processed lists for each case.

