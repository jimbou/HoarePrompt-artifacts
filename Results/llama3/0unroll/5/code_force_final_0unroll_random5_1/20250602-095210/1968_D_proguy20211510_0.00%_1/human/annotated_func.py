#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains four integers: n, k, P_B, P_S, followed by a list of n integers representing the permutation p, and another list of n integers representing the array a. n is a positive integer, k is a positive integer, P_B and P_S are positive integers less than or equal to n. The permutation p is a list of distinct integers from 1 to n in arbitrary order. The array a is a list of positive integers.
    YES, NO = 'YES', 'NO'
    MOD = 10 ** 9 + 7
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    for _ in range(int(input())):
        n, k, pb, ps = input().split()
        
        n, k, pb, ps = int(n), int(k), int(pb), int(ps)
        
        p = list(map(int, input().split()))
        
        a = list(map(int, input().split()))
        
        maxa = max(a)
        
        if a[pb - 1] == a[ps - 1] == maxa:
            print('Draw')
            continue
        elif a[pb - 1] == maxa:
            print('Bodya')
            continue
        elif a[ps - 1] == maxa:
            print('Sasha')
            continue
        
        b, s = [], []
        
        founds, foundb = False, False
        
        for i in range(k):
            if foundb and founds:
                b.append((k - (i + 1)) * maxa)
                s.append((k - (i + 1)) * maxa)
                break
            if foundb:
                b.append(maxa)
            elif a[pb - 1] == maxa:
                foundb = True
                b.append(a[pb - 1])
            else:
                b.append(a[pb - 1])
                pb = p[pb - 1]
            if founds:
                s.append(maxa)
            elif a[ps - 1] == maxa:
                founds = True
                s.append(a[ps - 1])
            else:
                s.append(a[ps - 1])
                ps = p[ps - 1]
        
        preb, pres = [], []
        
        sb, ss = 0, 0
        
        for i in range(len(s)):
            preb.append(sb + b[i])
            sb += b[i]
            pres.append(ss + s[i])
            ss += s[i]
        
        ptsb, ptss = [], []
        
        for i in range(len(pres)):
            rem = k - (i + 1)
            ptsb.append(preb[i] + rem * b[i])
            ptss.append(pres[i] + rem * s[i])
        
        maxs, maxb = max(ptss), max(ptsb)
        
        if maxs > maxb:
            print('Sasha')
        elif maxs < maxb:
            print('Bodya')
        else:
            print('Draw')
        
    #State: YES is 'YES', NO is 'NO', MOD is 1000000007, alpha is 'abcdefghijklmnopqrstuvwxyz', stdin is empty.

#Overall this is what the function does:Determines the winner of a game between two players, Bodya and Sasha, based on a given permutation and array of integers. The function takes no parameters but reads input from stdin, which contains multiple test cases. Each test case consists of four integers (n, k, P_B, P_S) followed by a permutation p and an array a. The function calculates the maximum score for each player and prints the winner ('Bodya', 'Sasha', or 'Draw') for each test case.

