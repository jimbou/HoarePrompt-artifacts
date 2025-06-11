#State of the program right berfore the function call: stdin contains an integer t, followed by t test cases. Each test case contains two integers n and k, followed by k lines, each containing n integers.
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
        
    #State: t is an integer greater than or equal to 0, n is an integer, m is 0, a1 is an integer, a2 is an integer, a3 is an integer, l1 is a list of integers with either a1 inserted at index idx2 or a2 inserted at index idx1, l2 is a list of integers with a2 inserted at index idx1 if the index of a1 in l3 is not less than the index of a2 in l3, otherwise l2 remains unchanged, l11 is a list of integers excluding a2, l22 is a list of integers excluding a1, idx1 is either -1 or some value, idx2 is either -1 or some value, p1 is either 0 or 1, p2 is either 0 or 1, i is n-1, val is an empty list, l is a list of integers with either a1 inserted at index idx2 or a2 inserted at index idx1, l3 is the second element in the last tuple in val, _ is 0, stdin is empty.

#Overall this is what the function does:This function reads input from stdin, processes multiple test cases, and determines whether a specific condition is met for each test case. It takes no arguments and returns no value, but instead prints 'yes' or 'no' to indicate whether the condition is satisfied for each test case. The function processes the input in a specific format, expecting an integer t followed by t test cases, each containing two integers n and k, followed by k lines of n integers. It then performs a series of comparisons and insertions on the input data to determine the outcome for each test case.

