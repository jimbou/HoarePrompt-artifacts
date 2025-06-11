#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of four lines. The first line contains four integers: n, k, P_B, P_S (1 <= P_B, P_S <= n <= 2*10^5, 1 <= k <= 10^9). The second line contains n integers p_1,...,p_n (1 <= p_i <= n). The third line contains n integers a_1,...,a_n (1 <= a_i <= 10^9).
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
        
    #State: The loop will execute 't' number of times, where 't' is the number of test cases provided in the input. For each test case, the loop will determine the winner of a game between 'Bodya' and 'Sasha' based on the given conditions. The output will be either 'Bodya', 'Sasha', or 'Draw', depending on the calculated values of 'bm' and 'sm'. The values of 'n', 'k', 'p', 'a', 'b', 's', 'sp', 'bp', 'bm', and 'sm' will be updated for each test case, but their initial values will be restored for the next test case.

#Overall this is what the function does:This function determines the winner of a game between 'Bodya' and 'Sasha' based on the given conditions for multiple test cases. It accepts the number of test cases, and for each test case, it takes four integers (n, k, P_B, P_S) and two lists of integers (p and a) as input. The function then calculates the values of 'bm' and 'sm' based on the given conditions and prints the winner as either 'Bodya', 'Sasha', or 'Draw' depending on the calculated values. The function repeats this process for the specified number of test cases.

