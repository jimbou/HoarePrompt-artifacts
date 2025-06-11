#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains four lines. The first line contains four integers: n, k, P_B, P_S (1 <= n <= 2 * 10^5, 1 <= k <= 10^9, 1 <= P_B, P_S <= n). The second line contains n integers p_1, ..., p_n (1 <= p_i <= n). The third line contains n integers a_1, ..., a_n (1 <= a_i <= 10^9).
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
        
    #State: The loop will execute 't' number of times, each time processing a test case from the standard input. For each test case, it will determine the winner of a game between 'Bodya' and 'Sasha' based on the given rules and print the result. The output will be a sequence of 't' lines, each containing the name of the winner or 'Draw' if the scores are equal. The values of 'n', 'k', 'p', 'a', 'b', 's', 'sp', 'bp', 'bm', and 'sm' will be updated for each test case, but their initial values will be lost after the loop finishes. The final state will only contain the output of the loop, which is the sequence of winners or 'Draw' for each test case.

#Overall this is what the function does:This function reads multiple test cases from standard input, each containing four lines of integers, and determines the winner of a game between 'Bodya' and 'Sasha' based on the given rules. It prints the result of each test case, either 'Bodya', 'Sasha', or 'Draw' if the scores are equal. The function processes each test case independently, updating variables accordingly, and outputs a sequence of winners or 'Draw' for each test case.

