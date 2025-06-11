#State of the program right berfore the function call: n is a positive integer, m is a non-negative integer such that m <= n*(n-1)/2, k is a positive integer, friendships is a list of m tuples, each tuple contains three positive integers a, b, and f such that 1 <= a, b <= n and a != b and 1 <= f <= 10^9.
    result = 0
    for i in range(m):
        a, b, f = friendships[i]
        
        result += f * (k * (k + 1) // 2) % MOD
        
    #State: n is a positive integer, m is a non-negative integer such that m <= n*(n-1)/2, k is a positive integer, friendships is a list of m tuples, each tuple contains three positive integers a, b, and f such that 1 <= a, b <= n and a != b and 1 <= f <= 10^9, result is sum(f * (k * (k + 1) // 2) % MOD for a, b, f in friendships), i is m
    return result % MOD
    #The program returns the remainder of the sum of products of friendship values and a quadratic expression of k, modulo MOD, where the sum is taken over all friendships in the list, and MOD is a constant value.

#Overall this is what the function does:Functionality: This function calculates the sum of products of friendship values and a quadratic expression of k, modulo MOD, for all friendships in the input list, and returns the remainder.

#State of the program right berfore the function call: n, m, and k are integers such that 2 <= n <= 10^5, 0 <= m <= min(10^5, n*(n-1)/2), and 1 <= k <= 2*10^5. friendships is a list of m lists, each containing three integers a_i, b_i, and f_i such that 1 <= a_i, b_i <= n and 1 <= f_i <= 10^9.
    t = int(input())
    for _ in range(t):
        n, m, k = map(int, input().split())
        
        friendships = [list(map(int, input().split())) for _ in range(m)]
        
        result = func_1(n, m, k, friendships)
        
        print(result)
        
    #State: n is an integer greater than or equal to 2 and less than or equal to 10^5, m is an integer greater than or equal to 0 and less than or equal to min(10^5, n*(n-1)/2), k is an integer greater than or equal to 1 and less than or equal to 2*10^5, friendships is a list of m lists, each containing three integers a_i, b_i, and f_i such that 1 <= a_i, b_i <= n and 1 <= f_i <= 10^9, t is an integer greater than or equal to 0, _ is t-1, result is the output of func_1(n, m, k, friendships), stdin is empty, and the output of func_1(n, m, k, friendships) is being printed.

#Overall this is what the function does:The function accepts four parameters: n, m, k, and friendships. It processes the input data and produces an output, which is then printed. The function does not modify the input variables n, m, k, or friendships. The output is determined by the function's internal logic, which is not explicitly described in the provided annotations. The function's purpose is to process the input data and generate a result, which is then printed to the console.

