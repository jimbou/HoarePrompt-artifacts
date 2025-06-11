#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains four integers (n, k, P_B, P_S) followed by two lists of n integers (p_1, ..., p_n) and (a_1, ..., a_n). n is a positive integer, k is a non-negative integer, 1 <= P_B, P_S <= n, and p_i and a_i are positive integers for all i.
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
        
    #State: t is a positive integer greater than or equal to 0, n is an integer greater than or equal to 0, p is a list of integers, a is a list of integers, s is the integer at index s in list p minus 1, b is the integer at index b in list p minus 1, i is n, k is decreased by n, sp is the integer at index s in list a times n, bp is the integer at index b in list a times n, bm is the integer at index b in list a times (k + n) plus the maximum of the integer at index b in list a times (k + n) and the integer at index b in list a times (k + n - 1) plus the integer at index b in list a, sm is the integer at index s in list a times (k + n) plus the maximum of the integer at index s in list a times (k + n) and the integer at index s in list a times (k + n - 1) plus the integer at index s in list a. If bm is greater than sm, 'Bodya' is printed. If bm is less than or equal to sm, 'Sasha' is printed if bm is less than sm, otherwise 'Draw' is printed.

#Overall this is what the function does:This function simulates a game between two players, Bodya and Sasha, based on the input provided. It accepts multiple test cases, each containing four integers (n, k, P_B, P_S) and two lists of n integers (p_1, ..., p_n) and (a_1, ..., a_n). The function then determines the winner of the game by calculating the scores of Bodya and Sasha based on the given rules and prints the result as either 'Bodya', 'Sasha', or 'Draw'.

