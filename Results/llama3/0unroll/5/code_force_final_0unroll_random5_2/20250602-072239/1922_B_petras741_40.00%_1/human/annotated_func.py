#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of two lines: the first line contains one integer n (1 ≤ n ≤ 3 * 10^5), and the second line contains n integers a_1, a_2, ..., a_n (0 ≤ a_i ≤ n).
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
        
    #State: The buffer is filled with the results of the calculations for each test case, and the stdin is empty.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer n followed by n integers. For each test case, it calculates the number of triplets that can be formed from the given integers and prints the result. If n is less than 3, it prints 0. The function processes all test cases and empties the standard input.

