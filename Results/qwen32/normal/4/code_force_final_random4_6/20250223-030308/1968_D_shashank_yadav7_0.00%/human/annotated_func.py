#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each of the t test cases, n, k, P_B, and P_S are integers such that 1 <= P_B, P_S <= n <= 2 * 10^5 and 1 <= k <= 10^9. p is a list of n integers such that 1 <= p_i <= n for each i from 1 to n. a is a list of n integers such that 1 <= a_i <= 10^9. The sum of all n values across all test cases does not exceed 2 * 10^5.
def func():
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
        
    #State: After all iterations, `t` is 0 (since all test cases have been processed), `n`, `k`, `b`, `s`, `p`, and `a` from the last test case are the ones used in the last iteration, `bm` and `sm` are the final accumulated values from the last test case, and the program has printed the result ("Bodya", "Sasha", or "Draw") for the last test case.
#Overall this is what the function does:The function processes `t` test cases. For each test case, it receives integers `n`, `k`, `P_B`, and `P_S`; a list `p` of `n` integers; and a list `a` of `n` integers. It calculates two cumulative scores, `bm` and `sm`, based on the provided values and rules, and prints "Bodya" if `bm` is greater, "Sasha" if `sm` is greater, or "Draw" if they are equal.

