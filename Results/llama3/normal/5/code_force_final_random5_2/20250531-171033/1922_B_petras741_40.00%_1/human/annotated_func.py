#State of the program right berfore the function call: stdin contains t test cases. Each test case contains two lines: the first line contains one integer n (1 ≤ n ≤ 3*10^5), and the second line contains n integers a_1, a_2, ..., a_n (0 ≤ a_i ≤ n). The sum of n over all test cases does not exceed 3*10^5.
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
        
    #State: t is 0, i is equal to the initial value of t, buffer is an empty list, stdin contains no input. For each test case, if n is greater than or equal to 3, q is a list of n+1 integers where each element at index w[j] is incremented by 1 for all j in range n, eta is a list containing all indices j from 0 to n where q[j] is greater than 0, and rho is the value of q at index eta[0] if eta_ln is 1, otherwise rho is the sum of all elements in q at indices in eta. If eta_ln is 1, the number of ways to choose 3 elements from n elements is printed, which is n * (n - 1) * (n - 2) // 6. Otherwise, the sum of the sum of q[eta[j]] * (q[eta[j]] - 1) * (q[eta[j]] - 2) // 6 and q[eta[j]] * (q[eta[j]] - 1) // 2 * rho for all j in range eta_ln is printed. If n is less than 3, 0 is printed.

#Overall this is what the function does:This function reads input from stdin, processes multiple test cases, and prints the number of ways to choose 3 elements from a given set of integers. For each test case, it reads an integer n and a list of n integers, then calculates the number of combinations of 3 elements that can be chosen from the list. If n is less than 3, it prints 0. Otherwise, it prints the total number of combinations, which is calculated by summing the combinations of 3 elements from each unique value in the list and the combinations of 2 elements from each unique value with the remaining elements.

