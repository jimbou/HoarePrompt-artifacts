#State of the program right berfore the function call: stdin contains t test cases. Each test case contains two lines. The first line contains an integer n. The second line contains n integers a_1, a_2, \dots, a_n. 1 <= t <= 10^4, 1 <= n <= 3 * 10^5, 0 <= a_i <= n. The sum of n over all test cases does not exceed 3 * 10^5.
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
        
    #State: The loop has executed t times, and for each test case, it has printed the number of ways to choose three distinct integers from the input list. The value of t remains unchanged, and the buffer list is still empty. The stdin contains no test cases, as they have all been consumed by the loop.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer n followed by n integers. It then calculates and prints the number of ways to choose three distinct integers from the input list for each test case. If a test case has less than three integers, it prints 0. After processing all test cases, the function does not return any value or modify any external state, but rather consumes all input test cases from standard input.

