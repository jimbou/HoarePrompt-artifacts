#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains four lines. The first line contains four integers: n, k, P_B, P_S. The second line contains n integers representing the permutation p. The third line contains n integers representing the array a.
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
        
    #State: Output State: The loop will execute t times, each time processing a test case from the input. The output will be a string indicating the winner of the game ('Bodya', 'Sasha', or 'Draw') for each test case. The variables n, k, b, s, p, a, sp, bp, bm, and sm will be updated accordingly for each test case, but their values will not be retained after each iteration. The final output state will be the last output string printed by the loop.

#Overall this is what the function does:This function simulates a game between two players, Bodya and Sasha, based on input test cases. For each test case, it processes the game state, updating variables to track the players' scores, and determines the winner of the game. The function then prints the result of each test case, indicating whether Bodya wins, Sasha wins, or the game ends in a draw. The function iterates through multiple test cases, processing each one independently and printing the corresponding result.

