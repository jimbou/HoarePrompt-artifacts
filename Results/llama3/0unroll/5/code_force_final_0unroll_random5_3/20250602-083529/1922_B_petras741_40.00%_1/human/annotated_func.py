#State of the program right berfore the function call: stdin contains t test cases. Each test case contains two lines. The first line contains one integer n. The second line contains n integers a_1, a_2, ..., a_n. t, n, and a_i are integers such that 1 <= t <= 10^4, 1 <= n <= 3 * 10^5, and 0 <= a_i <= n. The sum of n over all test cases does not exceed 3 * 10^5.
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
        
    #State: The loop has executed t iterations, and for each iteration, it has read two lines from stdin, processed the input, and printed the result. The buffer remains empty. The value of t is unchanged. The state of stdin is modified as t test cases have been read and processed. The output is printed to the console for each test case.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer n followed by n integers. It then calculates and prints the number of triplets that can be formed from the given integers, considering all possible combinations. If the number of integers n is less than 3, it prints 0. The function processes each test case independently and prints the result for each case.

