#State of the program right berfore the function call: stdin contains t test cases. Each test case consists of two lines: the first line contains one integer n, and the second line contains n integers a_1, a_2, ..., a_n.
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
        
    #State: t is an integer, stdin contains 0 test cases, buffer is a list, i is t-1, n is an integer equal to the input value, w is a list of integers equal to the input values. If n is at least 3, q is a list of n+1 integers where the value at index w[j] is the number of times w[j] appears in w for all j in range(n), j is either n or greater than 1000, eta is a list containing all values j in range(n+1) where q[j] is greater than 0, and if eta_ln is 1, the number of ways to choose 3 elements from n elements is printed. Otherwise, eta_ln is at least 2, rho is the sum of all values in q, and res is the sum of the value of q at index eta[j] multiplied by the value of q at index eta[j] minus 1, multiplied by the value of q at index eta[j] minus 2, all divided by 6, plus the value of q at index eta[j] multiplied by the value of q at index eta[j] minus 1, divided by 2, multiplied by the sum of all values in q up to eta[j-1] for all j in range(1, eta_ln), and if j is greater than 1000, we break out of the most internal loop or if statement, and res is printed. If n is less than 3, buffer is an empty list, and 0 is being printed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer n followed by n integers. For each test case, it calculates the number of ways to choose 3 elements from the given integers, taking into account the frequency of each integer. If n is less than 3, it prints 0. Otherwise, it prints the calculated result, which is the sum of the number of ways to choose 3 elements from each distinct integer value, plus the number of ways to choose 2 elements from each distinct integer value and 1 element from the remaining integers. The function processes all test cases and prints the results accordingly.

