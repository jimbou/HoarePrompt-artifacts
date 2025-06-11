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
        
    #State: The output state will be a series of pairs of lists, where each pair represents the output for a test case. Each list contains the rearranged elements from the input lists a and b, with the goal of maximizing the number of pairs of equal elements. The first list in each pair contains the rearranged elements from the first half of the input list, and the second list contains the rearranged elements from the second half of the input list. The number of pairs of equal elements in each list is maximized, with the constraint that the total number of pairs across both lists does not exceed 2k.

#Overall this is what the function does:This function takes multiple test cases as input, where each test case consists of two lines. The first line contains two integers n and k, and the second line contains 2n integers. The function rearranges the integers in each test case to maximize the number of pairs of equal elements, with the constraint that the total number of pairs across both lists does not exceed 2k. It then prints the rearranged lists for each test case, with the first list containing the rearranged elements from the first half of the input list and the second list containing the rearranged elements from the second half of the input list.

