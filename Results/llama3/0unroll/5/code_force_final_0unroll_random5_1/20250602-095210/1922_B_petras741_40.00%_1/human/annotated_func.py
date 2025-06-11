#State of the program right berfore the function call: stdin contains t test cases. Each test case contains two lines: the first line contains an integer n, and the second line contains n integers a_1, a_2, ..., a_n.
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
        
    #State: The loop has executed t times, and for each test case, it has printed the number of triplets that can be formed from the given array of integers. The value of t remains unchanged, and the buffer list is still empty. The stdin has been fully consumed and is now empty.

#Overall this is what the function does:This function reads a specified number of test cases from standard input, where each test case consists of an integer n followed by n integers. It then calculates and prints the number of unique triplets that can be formed from the given integers. If a test case has less than 3 integers, it prints 0. After processing all test cases, the function leaves the standard input empty and does not modify any external state.

