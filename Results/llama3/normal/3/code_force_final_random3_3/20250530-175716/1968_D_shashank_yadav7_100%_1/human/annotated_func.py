#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains four lines. The first line contains four space-separated integers: n, k, P_B, P_S. The second line contains n space-separated integers representing the permutation p. The third line contains n space-separated integers representing the array a. The integer k is a non-negative integer and n is a positive integer. 1 <= P_B, P_S <= n. The permutation p and array a contain integers from 1 to n.
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
        
    #State: t is a positive integer greater than or equal to 0, i is equal to t, n is a positive integer, k is an integer equal to 0, b is an integer between 0 and n-1, s is an integer between 0 and n-1, p is a list of integers from 1 to n, a is a list of integers from 1 to n, sp is an integer equal to the sum of all elements in a, bp is an integer equal to the sum of all elements in a, bm is an integer equal to the maximum of all possible products of elements in a and k, sm is an integer equal to the maximum of all possible products of elements in a and k. If bm is greater than sm, 'Bodya' is printed. If bm is less than sm, 'Sasha' is printed. Otherwise, 'Draw' is printed.

#Overall this is what the function does:This function determines the winner of a game between two players, 'Bodya' and 'Sasha', based on the maximum possible products of elements in an array and a given integer k. It takes multiple test cases as input, where each test case consists of four lines: the first line contains four space-separated integers (n, k, P_B, P_S), the second line contains a permutation p, the third line contains an array a, and the fourth line is not used. The function then simulates the game for each test case, updating the positions of 'Bodya' and 'Sasha' based on the permutation p and calculating the maximum possible products. Finally, it prints the winner of each game, either 'Bodya', 'Sasha', or 'Draw' if the maximum products are equal.

