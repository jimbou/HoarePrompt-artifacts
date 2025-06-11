#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case consists of two integers n and k (1 <= k <= n <= 2 * 10^5, n * k <= 2 * 10^5) followed by k lines, each containing n distinct integers from 1 to n.
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
        
    #State: The loop will execute 't' number of times, where 't' is an integer between 1 and 10^4 (inclusive). In each iteration, it will read two integers 'n' and 'k' from the standard input, where 'k' is between 1 and 'n' (inclusive) and 'n' is between 1 and 2 * 10^5 (inclusive). It will then read 'k' lines of 'n' distinct integers from 1 to 'n'. The loop will compare the integers in each line and print 'yes' if they are in the same order, and 'no' otherwise.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of two integers 'n' and 'k' followed by 'k' lines of 'n' distinct integers. It then checks if the integers in each line are in the same order, and prints 'yes' if they are, and 'no' otherwise. The function handles cases where 'k' is 1 or 2 separately, and for 'k' greater than 2, it inserts a missing element into one of the lines and checks if the resulting lines are in the same order.

