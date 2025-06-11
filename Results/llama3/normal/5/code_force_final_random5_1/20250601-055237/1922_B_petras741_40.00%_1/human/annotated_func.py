#State of the program right berfore the function call: stdin contains t+2*t*n integers, where t is a positive integer, n is a positive integer, and the remaining t*n integers are non-negative integers.
    t = int(input())
    buffer = []
    for i in range(t):
        n = int(input())
        
        w = [int(k) for k in input().split()]
        
        if n >= 3:
            q = {}
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
                    if j > 1000:
                        break
                print(res)
        else:
            print(0)
        
    #State: t is a positive integer, i is t-1, buffer is an empty list, n is an integer, w is a list of n integers, stdin is empty, eta is a list containing the integers from 0 to n, and rho is 1. If n is less than 3, 0 is printed. If n is 3 or more, a list q of n+1 integers is created where q[w[j]] is 1 for all j in range(n), and j is n. If eta_ln is 1, the number of combinations of 3 elements from a set of n elements, n * (n - 1) * (n - 2) // 6, is printed. Otherwise, rho is 1 + sum(q[eta[j]] for j in range(1, eta_ln)), res is sum(q[eta[j]] * (q[eta[j]] - 1) * (q[eta[j]] - 2) // 6 + q[eta[j]] * (q[eta[j]] - 1) // 2 * (1 + sum(q[eta[k]] for k in range(1, j))) for j in range(1, eta_ln)), and j is equal to eta_ln, and res is printed.

#Overall this is what the function does:This function reads input from stdin, processes it, and prints the result. It accepts a positive integer t, followed by t sets of input, each consisting of a positive integer n and a list of n non-negative integers. If n is less than 3, it prints 0. If n is 3 or more, it calculates and prints the number of combinations of 3 elements from the set of n elements, taking into account the frequency of each element. The function processes each set of input independently and prints the result for each set.

