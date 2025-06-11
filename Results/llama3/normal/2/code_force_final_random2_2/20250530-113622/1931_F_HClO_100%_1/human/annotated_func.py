#State of the program right berfore the function call: stdin contains one or more test cases. Each test case contains two integers n and k (1 <= k <= n <= 2 * 10^5, n * k <= 2 * 10^5) followed by k lines, each containing n integers (1 <= a_ij <= n, all a_ij are different).
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
        
    #State: `t` is an integer equal to 0, `m` is an integer greater than or equal to 2, `n` is an integer greater than or equal to 2, `_` is the current value of `m - 2`, `a1` is an integer, `l1` is a list of integers, `a2` is an integer, `l2` is a list of integers, `l11` is a list of integers, `l22` is a list of integers, `p1` is either 1 or 0, `p2` is either 1 or 0, `i` is the current value of `n - 1`, `val` is an empty list, `a3` is undefined, `l3` is undefined. If all `l3` were equal to the list of integers excluding `a3`, then 'yes' is printed. Otherwise, 'no' is printed.

#Overall this is what the function does:This function determines whether a set of matrices are permutations of each other. It reads input from stdin, where each test case consists of two integers n and k, followed by k lines of n integers. The function checks if all matrices are permutations of each other by comparing the rows of the matrices, excluding the first element of each row. If all matrices are permutations of each other, it prints 'yes', otherwise it prints 'no'. The function handles multiple test cases and ignores any remaining input after processing each test case.

