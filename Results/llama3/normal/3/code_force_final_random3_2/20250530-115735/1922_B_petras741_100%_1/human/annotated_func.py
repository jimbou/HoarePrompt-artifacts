#State of the program right berfore the function call: stdin contains t test cases. Each test case contains two inputs: first an integer n, then n integers a_1, a_2, ..., a_n. t, n and a_i are non-negative integers. 1 <= t <= 10^4, 1 <= n <= 3 * 10^5, and 0 <= a_i <= n. The sum of n over all test cases does not exceed 3 * 10^5.
    t = int(input())
    buffer = []
    for i in range(t):
        n = int(input())
        
        w = [int(k) for k in input().split()]
        
        if n >= 3:
            q = [(0) for j in range(n + 1)]
            for j in range(n):
                q[w[j]] += 1
            eta = []
            for j in range(n + 1):
                if q[j] > 0:
                    eta.append(j)
            eta_ln = len(eta)
            rho = q[eta[0]]
            if eta_ln == 1:
                print(n * (n - 1) * (n - 2) // 6)
            else:
                res = q[eta[0]] * (q[eta[0]] - 1) * (q[eta[0]] - 2) // 6
                for j in range(1, eta_ln):
                    res += q[eta[j]] * (q[eta[j]] - 1) * (q[eta[j]] - 2) // 6
                    res += q[eta[j]] * (q[eta[j]] - 1) // 2 * rho
                    rho += q[eta[j]]
                print(res)
        else:
            print(0)
        
    #State: t is 0, i is t, n is an integer from stdin, w is a list of integers from stdin, stdin contains 0 test cases, buffer is an empty list. If n is greater than or equal to 3, a list q of n+1 integers is created where the value at index w[j] is the number of times w[j] appears in w and the rest are 0. Then, a list eta containing all the indices j where q[j] is greater than 0 is created, and eta_ln is the number of indices j where q[j] is greater than 0. rho is either the number of times w[eta[0]] appears in w or the sum of q[eta[j]] for all j in range(eta_ln). If eta_ln is 1, the number of combinations of 3 elements from n elements which is n*(n-1)*(n-2)//6 is being printed. Otherwise, the number of combinations of 3 w[eta[0]] in w plus the sum of q[eta[j]] * (q[eta[j]] - 1) * (q[eta[j]] - 2) // 6 plus q[eta[j]] * (q[eta[j]] - 1) // 2 * rho for all j in range(1, eta_ln) is being printed. If n is less than 3, 0 is being printed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer n followed by n integers. It then calculates and prints the number of combinations of 3 elements that can be formed from the given integers, taking into account the frequency of each integer. If n is less than 3, it prints 0. The function processes all test cases and prints the results accordingly.

