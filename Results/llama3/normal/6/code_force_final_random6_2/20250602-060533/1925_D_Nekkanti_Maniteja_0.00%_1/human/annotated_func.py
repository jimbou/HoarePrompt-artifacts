#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains an integer t, followed by t sets of inputs. Each set of inputs contains an integer k, followed by k lines of input. Each line of input contains three integers: n, m, and k, followed by m lines of input, each containing three integers: a_i, b_i, and f_i.
    for i in range(int(input())):
        n, m, k = map(int, input().split())
        
        M = 10 ** 9 + 7
        
        c = pow(n * (n - 1) // 1, -1, M)
        
        s = 0
        
        a = 0
        
        for i in range(m):
            u, v, f = map(int, input().split())
            a += f
        
        for i in range(k):
            s = s + c * i * c * m + c * a
        
        print(s % M)
        
    #State: `i` is `t`, `t` is an integer, `n` is an integer, `m` is an integer, `k` is an integer, `M` is 1000000007, `c` is the modular multiplicative inverse of `n*(n-1)` modulo `M`, `s` is `k*(k-1)*c*i*c*m + k*c*a`, `a` is `m*f`, `u` is an integer, `v` is an integer, `f` is an integer, stdin contains no test cases, and the remainder of `s` divided by `M` is being printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case contains an integer t, followed by t sets of inputs. Each set of inputs contains an integer k, followed by k lines of input, each containing three integers: n, m, and k. The function then calculates the modular multiplicative inverse of n*(n-1) modulo 10^9 + 7, and uses this value to compute a sum s. The sum s is calculated as k*(k-1)*c*i*c*m + k*c*a, where c is the modular multiplicative inverse, i is the current test case number, m is the number of lines of input, and a is the sum of the third integer in each line of input. Finally, the function prints the remainder of s divided by 10^9 + 7 for each test case.

