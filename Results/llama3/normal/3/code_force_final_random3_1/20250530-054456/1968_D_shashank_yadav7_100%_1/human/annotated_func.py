#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of four lines. The first line contains four integers: n, k, P_B, P_S. The second line contains n integers representing the permutation p. The third line contains n integers representing the array a. n is a positive integer, k is a positive integer, 1 <= P_B, P_S <= n. The permutation p and array a are lists of positive integers.
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
        
    #State: t is a positive integer greater than or equal to 0, i is equal to t, n is an integer, b is an integer equal to p[p[p...[p[b] - 1] - 1] - 1...]] minus 1 minus n, s is an integer equal to p[p[p...[p[s] - 1] - 1] - 1...]] minus 1 minus n, p is a list of n integers, a is a list of n integers, sp is an integer equal to the value of a at index s plus a[s] plus a[s] plus a[s] plus ... plus a[s] t times, bp is an integer equal to the value of a at index b plus a[b] plus a[b] plus a[b] plus ... plus a[b] t times, bm is an integer equal to the maximum of its original value and a[p[p...[p[b] - 1] - 1] - 1...]] times (k-t+1) plus a[p[p...[p[b] - 1] - 1] - 1...]] plus a[p[p...[p[b] - 1] - 1] - 1...]] times k, sm is an integer equal to the maximum of its original value and a[p[p...[p[s] - 1] - 1] - 1...]] times (k-t+1) plus a[p[p...[p[s] - 1] - 1] - 1...]] plus a[p[p...[p[s] - 1] - 1] - 1...]] times k, and k is equal to -t+1. If bm is greater than sm, 'Bodya' is printed. If bm is less than or equal to sm, 'Sasha' is printed if bm is less than sm, otherwise 'Draw' is printed.

#Overall this is what the function does:This function simulates a game between two players, Bodya and Sasha, based on a given permutation and array. It takes multiple test cases as input, where each test case consists of four lines: the number of elements, the number of rounds, and the initial positions of Bodya and Sasha. The function then simulates the game for each test case, updating the positions of Bodya and Sasha based on the permutation, and calculating their scores. Finally, it prints the winner of each game, either Bodya, Sasha, or a draw, based on their final scores.

