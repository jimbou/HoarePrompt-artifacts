#State of the program right berfore the function call: n is a positive integer, m is a non-negative integer, k is a positive integer, friendships is a list of m tuples, each tuple contains three integers a, b, and f, where a and b are distinct integers between 1 and n (inclusive), and f is a positive integer.
    result = 0
    for i in range(m):
        a, b, f = friendships[i]
        
        result += f * (k * (k + 1) // 2) % MOD
        
    #State: Output State: `n` is a positive integer, `m` is a non-negative integer, `k` is a positive integer, `friendships` is a list of `m` tuples, each tuple contains three integers `a`, `b`, and `f`, where `a` and `b` are distinct integers between 1 and `n` (inclusive), and `f` is a positive integer, `result` is the sum of `f * (k * (k + 1) // 2) % MOD` for all tuples in `friendships`.
    return result % MOD
    #The program returns the sum of `f * (k * (k + 1) // 2) % MOD` for all tuples in `friendships`, where `f` is a positive integer, `k` is a positive integer, and `MOD` is a constant, modulo `MOD`.

#Overall this is what the function does:Calculates the sum of a weighted arithmetic series for each tuple in a list of friendships, where the weight is the product of a friendship factor and a triangular number, and returns the total sum modulo a constant.

#State of the program right berfore the function call: n, m, and k are integers such that 2 <= n <= 10^5, 0 <= m <= min(10^5, n*(n-1)/2), and 1 <= k <= 2*10^5. friendships is a list of m lists, each containing three integers a_i, b_i, and f_i, where 1 <= a_i, b_i <= n, a_i != b_i, and 1 <= f_i <= 10^9.
    t = int(input())
    for _ in range(t):
        n, m, k = map(int, input().split())
        
        friendships = [list(map(int, input().split())) for _ in range(m)]
        
        result = func_1(n, m, k, friendships)
        
        print(result)
        
    #State: The output state after the loop executes all the iterations is a list of `t` results, where each result is the output of the function `func_1` for the corresponding input values of `n`, `m`, `k`, and `friendships`. The values of `n`, `m`, `k`, and `friendships` are updated in each iteration of the loop, but the value of `t` remains unchanged.

#Overall this is what the function does:The function accepts four parameters: n, m, k, and friendships, where n, m, and k are integers and friendships is a list of lists containing integers. It processes the input data and returns a result, which is then printed as output. The function is called t times, with different input values for n, m, k, and friendships each time, and the results are printed in a list. The function's purpose is to perform some operation on the input data and produce an output, but the exact nature of this operation is not specified.

