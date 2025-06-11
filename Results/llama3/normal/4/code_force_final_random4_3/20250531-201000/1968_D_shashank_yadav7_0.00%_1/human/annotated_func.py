#State of the program right berfore the function call: stdin contains a number of test cases t, followed by t test cases. Each test case contains four integers n, k, P_B, P_S, followed by two lists of n integers p and a. n, k, P_B, P_S are positive integers, 1 <= n <= 2*10^5, 1 <= k <= 10^9, 1 <= P_B, P_S <= n. p is a permutation of integers from 1 to n. a is a list of positive integers.
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
            bm += max(bm, a[b] * k + bp)
            sm += max(sm, a[s] * k + sp)
            sp += a[s]
            bp += a[b]
        
        if bm > sm:
            print('Bodya')
        elif bm < sm:
            print('Sasha')
        else:
            print('Draw')
        
    #State: t is 0, i is 0, stdin is empty, n is a positive integer, b is a positive integer equal to p[p[p...[p[b] - 1] - 1] - 1] - 1, s is a positive integer equal to p[p[p...[p[s] - 1] - 1] - 1] - 1, p is a list of n integers, a is a list of n positive integers, sp is a positive integer equal to a[s] + a[p[s] - 1] + a[p[p[s] - 1] - 1] + ... + a[p[p...[p[s] - 1]], bp is a positive integer equal to a[b] + a[p[b] - 1] + a[p[p[b] - 1] - 1] + ... + a[p[p...[p[b] - 1]], bm is a positive integer equal to max(0, a[p[p...[p[b] - 1] - 1]] * (k-n+1) + a[p[p...[p[b] - 1] - 1]] + ... + a[p[b] - 1] * (k-1) + bp), sm is a positive integer equal to max(0, a[p[p...[p[s] - 1] - 1]] * (k-n+1) + a[p[p...[p[s] - 1] - 1]] + ... + a[p[s] - 1] * (k-1) + sp), k is -n+1.

#Overall this is what the function does:This function determines the winner of a game between two players, 'Bodya' and 'Sasha', based on the maximum score they can achieve by traversing a permutation of integers and accumulating points. The function takes no explicit parameters but reads input from stdin, which contains the number of test cases, followed by the test cases themselves. Each test case consists of four integers (n, k, P_B, P_S) and two lists of n integers (p and a). The function calculates the maximum scores for both players and prints the winner ('Bodya', 'Sasha', or 'Draw') for each test case.

