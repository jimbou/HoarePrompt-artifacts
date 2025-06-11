#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of four lines. The first line contains four space-separated integers: n, k, P_B, P_S. The second line contains n space-separated integers representing the permutation p. The third line contains n space-separated integers representing the array a. The integer n is a positive integer, k is a positive integer, P_B and P_S are positive integers such that 1 <= P_B, P_S <= n.
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
        
    #State: t is 0, i is equal to the initial value of t, n is a positive integer, k is a negative integer, b is the value of p at index b minus 1 minus 1 ... minus 1 (n times), s is the value of p at index s minus 1 minus 1 ... minus 1 (n times), p is a list of n integers, a is a list of n integers, sp is the value of a at index s plus the value of a at index s plus the value of a at index s ... plus the value of a at index s (n times), bp is the value of a at index b plus the value of a at index b plus the value of a at index b ... plus the value of a at index b (n times), bm is the maximum value between the value of a at index b multiplied by k plus the value of a at index b plus the value of a at index b ... plus the value of a at index b and the original value of bm, sm is the maximum value between the value of a at index s multiplied by k plus the value of a at index s plus the value of a at index s ... plus the value of a at index s and the original value of sm.

#Overall this is what the function does:This function determines the winner of a game between two players, Bodya and Sasha, based on the maximum score they can achieve by moving through a permutation of indices and accumulating values from an array. The function takes no parameters and returns no values, but instead prints the winner of the game for each test case. The game is played for multiple test cases, each consisting of four lines of input: the number of indices, the number of moves, and the starting indices for Bodya and Sasha, followed by the permutation of indices and the array of values. The function calculates the maximum score for each player by simulating their moves and accumulating values, and then prints the winner of the game based on their maximum scores.

