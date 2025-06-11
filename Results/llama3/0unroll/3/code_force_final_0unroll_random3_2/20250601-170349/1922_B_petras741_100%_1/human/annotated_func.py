#State of the program right berfore the function call: stdin contains t test cases. Each test case contains two lines: the first line contains an integer n (1 <= n <= 3 * 10^5), and the second line contains n space-separated integers a_1, a_2, ..., a_n (0 <= a_i <= n). The sum of n over all test cases does not exceed 3 * 10^5.
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
        
    #State: buffer is a list containing t-1 test cases, each test case is a string containing the number of ways to choose three distinct numbers from the given list of numbers, stdin is empty, t is still an integer but its value is not changed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer n followed by a list of n integers. For each test case, it calculates the number of ways to choose three distinct numbers from the given list and prints the result. If the list contains less than three elements, it prints 0. The function processes all test cases and empties the standard input.

