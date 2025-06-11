#State of the program right berfore the function call: n is a positive integer, m is a non-negative integer, k is a positive integer, friendships is a list of m tuples, each tuple containing three positive integers a, b, and f, where a and b are distinct and 1 <= a, b <= n, and 1 <= f <= 10^9.
    result = 0
    for i in range(m):
        a, b, f = friendships[i]
        
        result += f * (k * (k + 1) // 2) % MOD
        
    #State: n is a positive integer, m is a non-negative integer, k is a positive integer, friendships is a list of m tuples, each tuple containing three positive integers a, b, and f, where a and b are distinct and 1 <= a, b <= n, and 1 <= f <= 10^9, result is equal to the sum of f * (k * (k + 1) // 2) % MOD for all tuples in friendships, i is m - 1
    return result % MOD
    #The program returns the remainder of the sum of f * (k * (k + 1) // 2) for all tuples in friendships, divided by MOD, where f is a positive integer between 1 and 10^9, k is a positive integer, and MOD is a constant.

#Overall this is what the function does:This function calculates the sum of a weighted arithmetic series for each tuple in a list of friendships, where the weight is the product of a frequency value and the sum of the first k positive integers, and returns the remainder of this sum divided by a constant modulus. The function takes as input a positive integer n, a non-negative integer m, a positive integer k, and a list of m tuples containing three positive integers a, b, and f, and returns a single integer value.

#State of the program right berfore the function call: n, m, and k are positive integers, friendships is a list of lists of three integers, where each sublist contains the indices of a pair of children who are friends and their friendship value, 1 <= n <= 10^5, 0 <= m <= min(10^5, n(n-1)/2), 1 <= k <= 2*10^5, 1 <= f_i <= 10^9, and a_i != b_i, 1 <= a_i, b_i <= n.
    t = int(input())
    for _ in range(t):
        n, m, k = map(int, input().split())
        
        friendships = [list(map(int, input().split())) for _ in range(m)]
        
        result = func_1(n, m, k, friendships)
        
        print(result)
        
    #State: n, m, and k are integers, friendships is a list of lists of three integers, result is the return value of func_1(n, m, k, friendships), t is an integer greater than or equal to 0, _ is t-1, and the return value of func_1(n, m, k, friendships) which is stored in result is being printed.

#Overall this is what the function does:This function accepts four parameters: n, m, k, and friendships. It processes the input data, which includes the number of children (n), the number of friendships (m), a value k, and a list of friendships where each friendship is represented by a list of three integers containing the indices of two children and their friendship value. The function then returns a result, which is printed as output. The purpose of the function is to analyze the friendships and return a value based on the input data. The final state of the program is that the result of the function is printed, and the input variables n, m, k, and friendships are unchanged.

