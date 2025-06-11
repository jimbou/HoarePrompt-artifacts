#State of the program right berfore the function call: n is a positive integer, m is a non-negative integer such that m <= n*(n-1)/2, k is a positive integer, friendships is a list of m tuples, each tuple containing three positive integers a, b, and f such that a != b, 1 <= a, b <= n, and 1 <= f <= 10^9.
    result = 0
    for i in range(m):
        a, b, f = friendships[i]
        
        result += f * (k * (k + 1) // 2) % MOD
        
    #State: n is a positive integer, m is a non-negative integer such that m <= n*(n-1)/2, k is a positive integer, friendships is a list of m tuples, each tuple containing three positive integers a, b, and f such that a != b, 1 <= a, b <= n, and 1 <= f <= 10^9, result is the original value of result plus the sum of f * (k * (k + 1) // 2) % MOD for all tuples in friendships, i is m-1, a is the first element of the tuple at index m-1 in friendships, b is the second element of the tuple at index m-1 in friendships, f is the third element of the tuple at index m-1 in friendships.
    return result % MOD
    #The program returns the result modulo MOD, where result is the original value of result plus the sum of f * (k * (k + 1) // 2) % MOD for all tuples in friendships, and MOD is a constant value.

#Overall this is what the function does:Functionality: This function calculates the sum of a weighted sum of friendships, where each friendship is weighted by the product of the friendship value and a triangular number (k * (k + 1) // 2), and returns the result modulo a constant value MOD. The function takes as input a positive integer n, a non-negative integer m, a positive integer k, and a list of m tuples representing friendships, each containing three positive integers a, b, and f. The function returns a single value, which is the result of the calculation modulo MOD.

#State of the program right berfore the function call: n is a positive integer, m is a non-negative integer such that m <= n*(n-1)/2, k is a positive integer, friendships is a list of m lists, each containing three positive integers a, b, and f such that a != b, 1 <= a, b <= n, and 1 <= f <= 10^9.
    t = int(input())
    for _ in range(t):
        n, m, k = map(int, input().split())
        
        friendships = [list(map(int, input().split())) for _ in range(m)]
        
        result = func_1(n, m, k, friendships)
        
        print(result)
        
    #State: n is a positive integer equal to the first integer from stdin, m is a non-negative integer equal to the second integer from stdin, k is a positive integer equal to the third integer from stdin, friendships is a list of m lists, each containing three positive integers a, b, and f such that a != b, 1 <= a, b <= n, and 1 <= f <= 10^9, t is equal to 0, result is the output of func_1(n, m, k, friendships), stdin is empty, and the result of func_1(n, m, k, friendships) is being printed.

#Overall this is what the function does:The function `func_1` accepts four parameters: a positive integer `n`, a non-negative integer `m` where `m <= n*(n-1)/2`, a positive integer `k`, and a list of `m` lists `friendships` where each sublist contains three positive integers `a`, `b`, and `f` such that `a != b`, `1 <= a, b <= n`, and `1 <= f <= 10^9`. The function returns a result, which is then printed. The function does not modify the input variables `n`, `m`, `k`, or `friendships`. The purpose of the function is to process the input data and produce an output based on the given parameters and friendships list. The final state of the program after the function concludes is that the result of the function is being printed, and the input variables remain unchanged.

