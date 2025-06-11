#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains four integers (n, k, P_B, P_S) on the first line, a permutation p of length n on the second line, and an array a of length n on the third line. n is a positive integer, k is a positive integer, P_B and P_S are positive integers such that 1 <= P_B, P_S <= n. p is a permutation of length n, and a is an array of positive integers.
    t = int(input())
    for i in range(t):
        n, k, b, s = list(map(int, input().split()))
        
        p = list(map(int, input().split()))
        
        a = list(map(int, input().split()))
        
        b -= 1
        
        s -= 1
        
        sp = a[s]
        
        bp = a[b]
        
        bm = a[b] * k
        
        sm = a[s] * k
        
        for i in range(n):
            k -= 1
            if k == 0:
                break
            b = p[b] - 1
            s = p[s] - 1
            bm = max(bm, a[b] * k + bp)
            sm = max(sm, a[s] * k + sp)
            sp += a[s]
            bp += a[b]
        
        if bm > sm:
            print('Bodya')
        elif bm < sm:
            print('Sasha')
        else:
            print('Draw')
        
    #State: The loop will execute t times, and after each execution, it will print either 'Bodya', 'Sasha', or 'Draw' depending on the values of bm and sm. The values of t, n, k, P_B, P_S, p, and a will remain unchanged. The values of b, s, sp, bp, bm, and sm will be reset to their initial values at the beginning of each iteration.

#Overall this is what the function does:This function simulates a game between two players, Bodya and Sasha, based on the input test cases. It takes no parameters and returns no values. For each test case, it reads four integers (n, k, P_B, P_S), a permutation p of length n, and an array a of length n. It then simulates the game by iterating through the permutation and updating the scores of Bodya and Sasha. After each iteration, it prints the winner of the game ('Bodya', 'Sasha', or 'Draw') based on the final scores. The function repeats this process for the specified number of test cases (t).

