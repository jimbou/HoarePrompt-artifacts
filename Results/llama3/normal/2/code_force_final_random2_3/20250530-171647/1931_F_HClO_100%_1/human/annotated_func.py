#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case consists of two integers n and k (1 <= k <= n <= 2 * 10^5, n * k <= 2 * 10^5) followed by k lines, each containing n integers (1 <= a_ij <= n, all a_ij are different).
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        
        if m == 1:
            input()
            print('yes')
            continue
        
        a1, *l1 = map(int, input().split())
        
        a2, *l2 = map(int, input().split())
        
        l11 = [i for i in l1 if i != a2]
        
        l22 = [i for i in l2 if i != a1]
        
        if l11 != l22:
            for _ in range(m - 2):
                input()
            print('no')
            continue
        
        idx1 = idx2 = -1
        
        p1 = p2 = 0
        
        for i in range(n - 1):
            if i + max(p1, p2) == n - 1:
                break
            if l1[i + p1] != l2[i + p2]:
                if l1[i + p1] == a2 and l2[i + p2] == a1:
                    idx1 = idx2 = i
                    break
                else:
                    if l1[i + p1] == a2:
                        idx1 = i
                        p1 = 1
                    else:
                        idx2 = i
                        p2 = 1
                    if idx1 >= 0 and idx2 >= 0:
                        break
        
        val = []
        
        if idx1 == -1 and idx2 != -1:
            idx1 = n - 2
        
        if idx2 == -1 and idx1 != -1:
            idx2 = n - 2
        
        if idx1 < idx2:
            l2.insert(idx1, a2)
            l = l2
        elif idx1 > idx2:
            l1.insert(idx2, a1)
            l = l1
        else:
            if m == 2:
                print('yes')
                continue
            a3, *l3 = map(int, input().split())
            if l3.index(a1) < l3.index(a2):
                l1.insert(idx2, a1)
                l = l1
            else:
                l2.insert(idx1, a2)
                l = l2
            val.append((a3, l3))
            m -= 1
        
        for _ in range(m - 2):
            a3, *l3 = map(int, input().split())
            val.append((a3, l3))
        
        for a3, l3 in val:
            if l3 != [i for i in l if i != a3]:
                print('no')
                break
        else:
            print('yes')
        
    #State: t is an integer between 1 and 10^4, stdin is empty, m is 1, n is an integer, a1 is an integer, a2 is an integer, l11 is a list of integers, l22 is a list of integers, val is a list of tuples, a3 is the last a3 in the last tuple, l3 is the last l3 in the last tuple, p1 is either 0 or 1, p2 is either 0 or 1, idx1 is either -1, n - 2, or its original value, idx2 is either -1, n - 2, or its original value, and either 'yes' or 'no' is printed.

#Overall this is what the function does:This function reads input from stdin, processes it, and prints 'yes' or 'no' for each test case. It accepts an integer t (1 <= t <= 10^4) followed by t test cases. Each test case consists of two integers n and k (1 <= k <= n <= 2 * 10^5, n * k <= 2 * 10^5) followed by k lines, each containing n integers (1 <= a_ij <= n, all a_ij are different). The function checks if the input data satisfies certain conditions and prints 'yes' if the conditions are met, otherwise it prints 'no'.

