#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains four integers (n, k, P_B, P_S) on the first line, a list of n integers (p_1, ..., p_n) on the second line, and a list of n integers (a_1, ..., a_n) on the third line. n is a positive integer, k is a non-negative integer, 1 <= P_B, P_S <= n. p_i and a_i are positive integers for all i.
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
        
    #State: The loop will execute until there are no more test cases in the input. After the loop finishes executing, the output state will be the same as the initial state, with the addition of the results of the loop's execution. The results will be a series of 'Sasha', 'Bodya', or 'Draw' printed to the console, depending on the outcome of each test case. The loop will not modify any of the input variables, so the state of the input will remain unchanged.

#Overall this is what the function does:This function processes multiple test cases from standard input, each containing four integers (n, k, P_B, P_S) and two lists of n integers (p_1, ..., p_n) and (a_1, ..., a_n). It determines the winner of a game based on the values of a_1, ..., a_n and the indices P_B and P_S, and prints the result as 'Sasha', 'Bodya', or 'Draw' for each test case. The function does not modify the input variables and only prints the results to the console.

