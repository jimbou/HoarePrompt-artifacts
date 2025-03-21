#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each test case, n and k are positive integers such that 1 ≤ n, k ≤ 10^{18}.
def func():
    t = int(input())
    for _ in range(t):
        n, k = map(int, stdin.readline().split())
        
        rep = 0
        
        number = 0
        
        tab = []
        
        while n != 0 and k > 0 and rep < 60 and n >= k:
            Min, Max = min(n // k, k), max(int(n / k), k)
            if Max == k and n * Min <= k:
                number = Min
                k = k - Max
            else:
                number = Max
                k = k - Min
            tab.append(str(number))
            n -= Min * Max
            rep += 1
        
        if k == 0:
            print('YES')
            print(len(tab))
            for i in tab:
                print(i, end=' ')
        else:
            print('NO')
        
    #State: The output state depends on the input values of `n` and `k` for each iteration. If `n` becomes zero before `k` reaches zero or `rep` reaches 60, it prints 'YES' followed by the length of `tab` and the elements in `tab`. Otherwise, it prints 'NO'. The value of `t` will be the number of such iterations performed.
#Overall this is what the function does:The function processes up to 1000 test cases, where each test case consists of integers \( n \) and \( k \). For each test case, it repeatedly divides \( n \) by \( k \) (or vice versa) and records the quotient in a list until either \( n \) becomes less than \( k \), \( n \) is exhausted, or 60 iterations are reached. If \( n \) becomes zero before \( k \) or the maximum iterations are reached, it prints 'YES' followed by the length of the recorded quotients and the quotients themselves. Otherwise, it prints 'NO'. The function does not return any value but modifies and prints the results based on the input values.

