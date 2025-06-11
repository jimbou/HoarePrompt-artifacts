#State of the program right berfore the function call: stdin contains an integer t, followed by t sets of inputs. Each set of inputs contains four integers n, k, P_B, P_S, followed by two lists of n integers p_1,...,p_n and a_1,...,a_n. 1 <= t <= 10^4, 1 <= n <= 2 * 10^5, 1 <= k <= 10^9, 1 <= P_B, P_S <= n, 1 <= p_i, a_i <= n.
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
        
    #State: t is an integer between 1 and 10^4 (inclusive), i is equal to t, n is an integer, b is the integer at index b in list p minus t, s is the integer at index s in list p minus t, p is a list of integers, a is a list of integers, sp is the integer at index s in list a plus t times a[s], bp is the integer at index b in list a plus t times a[b], bm is the maximum of its original value and the sum of a[b] * k + bp for all k from t-1 to 1, sm is the maximum of its original value and the sum of a[s] * k + sp for all k from t-1 to 1, k is 0. If bm is greater than sm, 'Bodya' is printed. If bm is less than sm, 'Sasha' is printed. Otherwise, 'Draw' is printed.

#Overall this is what the function does:This function simulates a game between two players, Bodya and Sasha, based on input parameters. It accepts a number of test cases (t), and for each test case, it reads in the number of rounds (n), a constant (k), and the initial positions of Bodya (P_B) and Sasha (P_S) on a circular track. It also reads in two lists of integers representing the track's layout (p) and the points awarded at each position (a). The function then simulates the game, moving Bodya and Sasha around the track according to the layout and updating their scores based on the points awarded at each position. After the simulation, it prints out the winner of the game ('Bodya', 'Sasha', or 'Draw' if the scores are tied).

