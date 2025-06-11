#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains four integers: n, k, P_B, P_S (1 <= P_B, P_S <= n <= 2*10^5, 1 <= k <= 10^9). The next line contains n integers p_1,...,p_n (1 <= p_i <= n) - elements of the permutation p. The next line contains n integers a_1,...,a_n (1 <= a_i <= 10^9) - elements of array a.
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
        
    #State: The loop will execute 't' number of times, each time processing a test case from the standard input. For each test case, it will read four integers (n, k, P_B, P_S), then two lists of 'n' integers each (p and a). It will then simulate a game between 'Bodya' and 'Sasha', updating their scores based on the values in the lists and the number of rounds 'k'. After each test case, it will print the winner of the game ('Bodya', 'Sasha', or 'Draw') based on their final scores.

#Overall this is what the function does:This function simulates a game between two players, 'Bodya' and 'Sasha', for multiple test cases. For each test case, it reads the number of rounds, the initial positions of the players, and two lists of integers representing a permutation and an array. It then updates the players' scores based on the values in the lists and the number of rounds, and prints the winner of the game ('Bodya', 'Sasha', or 'Draw') based on their final scores. The function processes multiple test cases from the standard input and prints the result of each game.

