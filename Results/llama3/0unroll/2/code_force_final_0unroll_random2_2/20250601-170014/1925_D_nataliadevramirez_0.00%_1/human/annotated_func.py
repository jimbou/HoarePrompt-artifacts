#State of the program right berfore the function call: n and m are non-negative integers, k is a positive integer, friendships is a list of 3-element tuples, where each tuple contains three integers a, b, and f, such that 1 <= a, b <= n, a != b, and 1 <= f <= 10^9.
    result = 0
    for i in range(m):
        a, b, f = friendships[i]
        
        result += f * (k * (k + 1) // 2) % MOD
        
    #State: Output State: `n` and `m` are non-negative integers, `k` is a positive integer, `friendships` is a list of 3-element tuples, where each tuple contains three integers `a`, `b`, and `f`, such that 1 <= `a`, `b` <= `n`, `a` != `b`, and 1 <= `f` <= 10^9, `result` is the sum of `f * (k * (k + 1) // 2) % MOD` for all tuples in `friendships`.
    return result % MOD
    #The program returns the sum of f * (k * (k + 1) // 2) % MOD for all tuples in friendships, where MOD is the modulus value, k is a positive integer, and f is a value between 1 and 10^9, a and b are integers between 1 and n, and n and m are non-negative integers, and the result is taken modulo MOD.

#Overall this is what the function does:This function calculates the sum of a weighted value for each friendship in a list, where the weight is determined by a formula involving a positive integer k and a modulus value MOD. The function takes in parameters n, m, k, and friendships, where n and m are non-negative integers, k is a positive integer, and friendships is a list of 3-element tuples containing integers a, b, and f. The function returns the sum of f * (k * (k + 1) // 2) % MOD for all tuples in friendships, taken modulo MOD. The function does not modify the input variables n, m, k, or friendships.

#State of the program right berfore the function call: n, m and k are integers such that 2 <= n <= 10^5, 0 <= m <= min(10^5, n*(n-1)/2), 1 <= k <= 2*10^5. friendships is a list of m lists, each containing three integers a, b, and f such that 1 <= a, b <= n, a != b, and 1 <= f <= 10^9.
    t = int(input())
    for _ in range(t):
        n, m, k = map(int, input().split())
        
        friendships = [list(map(int, input().split())) for _ in range(m)]
        
        result = func_1(n, m, k, friendships)
        
        print(result)
        
    #State: Output State: The final output state after the loop executes all the iterations will be the result of the last iteration of the loop, which is the output of the function `func_1` with the last set of input values for `n`, `m`, `k`, and `friendships`. The values of `n`, `m`, `k`, and `friendships` will be the last values read from the input, and the value of `t` will be the number of iterations of the loop. The state of other variables in the precondition that are not affected by the loop head and body will remain unchanged.

#Overall this is what the function does:The function `func_1` accepts four parameters: `n`, `m`, `k`, and `friendships`, where `n` and `m` are integers, `k` is an integer, and `friendships` is a list of lists containing three integers each. The function processes the input values and returns a result, which is then printed as output. The function's purpose is to perform some operation on the input values and produce an output based on the processed data. The final state of the program after the function concludes is that the output of the function is printed, and the values of `n`, `m`, `k`, and `friendships` remain unchanged.

