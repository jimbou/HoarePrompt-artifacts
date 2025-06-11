#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line contains one integer n (1 ≤ n ≤ 3 * 10^5). The second line contains n integers a_1, a_2, …, a_n (0 ≤ a_i ≤ n). The sum of n over all test cases does not exceed 3 * 10^5.
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
        
    #State: t is an integer greater than or equal to 0, i is t-1, buffer is an empty list, n is an integer, w is a list of integers, stdin contains multiple test cases with two lines less than before. If n is less than 3, the number 0 is printed. If n is greater than or equal to 3, a list q of n+1 integers is created where the value at index w[j] is t for j in range n, and a list eta containing the values j for j in range n+1 where q[j] is greater than 0 is created. If the length of eta is 1, the number of combinations of 3 items that can be chosen from a set of n items is being printed. Otherwise, the length of eta is at least 2, and the result of a calculation involving the values in q and eta is being printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two lines. The first line contains an integer n, and the second line contains n integers. The function then calculates and prints the number of combinations of 3 items that can be chosen from the set of n items, considering the frequency of each item. If n is less than 3, it prints 0. The function processes all test cases and prints the results accordingly.

