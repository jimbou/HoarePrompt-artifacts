#State of the program right berfore the function call: stdin contains a number of test cases t, and for each test case, it contains four integers n, k, P_B, P_S, a permutation p_1,\dots,p_n, and an array a_1,\dots,a_n. 1 <= t <= 10^4, 1 <= n <= 2 * 10^5, 1 <= k <= 10^9, 1 <= P_B, P_S <= n, 1 <= p_i <= n, and 1 <= a_i <= 10^9.
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
        
    #State: The loop iterates t times, where t is the number of test cases provided in the input. After each iteration, the loop prints 'Sasha' if the maximum value in ptss is greater than the maximum value in ptsb, 'Bodya' if the maximum value in ptss is less than the maximum value in ptsb, and 'Draw' otherwise. The loop then reads the next set of inputs from stdin and repeats the process until all test cases have been processed.

#Overall this is what the function does:Determines the winner of a game between two players, 'Bodya' and 'Sasha', based on the maximum value of their respective scores, which are calculated by iterating through a permutation and an array. The function takes no parameters and returns no values, but instead prints the result of each test case to the standard output. The possible outcomes are 'Bodya', 'Sasha', or 'Draw', depending on whether the maximum score of 'Bodya' is greater than, less than, or equal to the maximum score of 'Sasha', respectively.

