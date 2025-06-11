#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of four lines. The first line contains four integers: n, k, P_B, P_S. The second line contains n integers representing the permutation p. The third line contains n integers representing the array a. n is a positive integer, k is a non-negative integer, 1 <= P_B, P_S <= n. The permutation p and array a are lists of integers.
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
        
    #State: The loop will execute t times, each time processing a test case from the input. After all iterations, the loop will have printed out the winner of each test case, either 'Bodya', 'Sasha', or 'Draw', based on the calculated values of bm and sm. The values of n, k, b, s, p, a, sp, bp, bm, and sm will be updated for each test case, but their initial values will be lost after the loop finishes. The final output will be a series of lines, each containing the result of a test case.

#Overall this is what the function does:This function processes multiple test cases from standard input, each consisting of four lines of integers. For each test case, it calculates the maximum score that can be achieved by two players, 'Bodya' and 'Sasha', based on a given permutation and array. The function then prints out the winner of each test case, either 'Bodya', 'Sasha', or 'Draw', depending on the calculated scores. After processing all test cases, the function outputs a series of lines, each containing the result of a test case.

