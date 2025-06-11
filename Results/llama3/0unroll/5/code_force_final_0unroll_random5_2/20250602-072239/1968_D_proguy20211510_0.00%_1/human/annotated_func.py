#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of four lines. The first line contains four space-separated integers: n, k, P_B, P_S (1 <= n, k, P_B, P_S <= 2 * 10^5). The second line contains n space-separated integers p_1, ..., p_n (1 <= p_i <= n). The third line contains n space-separated integers a_1, ..., a_n (1 <= a_i <= 10^9).
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

#Overall this is what the function does:Determines the winner of a game between two players, Bodya and Sasha, based on their scores and a set of rules. The function reads multiple test cases from standard input, each consisting of four lines: the number of players, the number of rounds, and the initial scores of Bodya and Sasha. It then simulates the game, updating the scores according to the rules, and prints the winner of each test case: either 'Bodya', 'Sasha', or 'Draw' if the scores are tied.

