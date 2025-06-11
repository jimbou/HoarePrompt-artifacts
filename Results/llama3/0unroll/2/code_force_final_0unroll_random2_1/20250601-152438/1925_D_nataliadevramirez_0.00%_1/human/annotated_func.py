#State of the program right berfore the function call: n is a positive integer, m is a non-negative integer, k is a positive integer, friendships is a list of m tuples where each tuple contains three positive integers a, b, and f such that 1 <= a, b <= n and 1 <= f <= 10^9.
    result = 0
    for i in range(m):
        a, b, f = friendships[i]
        
        result += f * (k * (k + 1) // 2) % MOD
        
    #State: Output State: `n` is a positive integer, `m` is a non-negative integer, `k` is a positive integer, `friendships` is a list of `m` tuples where each tuple contains three positive integers `a`, `b`, and `f` such that 1 <= `a`, `b` <= `n` and 1 <= `f` <= 10^9, `result` is the sum of `f * (k * (k + 1) // 2) % MOD` for all tuples `(a, b, f)` in `friendships`.
    return result % MOD
    #The program returns the sum of f * (k * (k + 1) // 2) % MOD for all tuples (a, b, f) in friendships, where MOD is a modulus value, k is a positive integer, f is a positive integer between 1 and 10^9, and the sum is taken modulo MOD.

#Overall this is what the function does:This function calculates the sum of a weighted arithmetic series for each tuple in a list of friendships, where the weight is the frequency of the friendship, and returns the total sum modulo a given modulus value. The function takes four parameters: a positive integer n, a non-negative integer m, a positive integer k, and a list of m tuples representing friendships, where each tuple contains three positive integers a, b, and f. The function returns a single value, which is the sum of f * (k * (k + 1) // 2) % MOD for all tuples (a, b, f) in friendships, taken modulo MOD.

#State of the program right berfore the function call: n is a positive integer, m is a non-negative integer such that m <= n*(n-1)/2, k is a positive integer, and friendships is a list of m lists, each containing three positive integers a, b, and f such that a != b, 1 <= a, b <= n, and 1 <= f <= 10^9.
    t = int(input())
    for _ in range(t):
        n, m, k = map(int, input().split())
        
        friendships = [list(map(int, input().split())) for _ in range(m)]
        
        result = func_1(n, m, k, friendships)
        
        print(result)
        
    #State: The output state after the loop executes all the iterations is that the variable 'result' will hold the output of the function func_1 for the last iteration of the loop, and the variables 'n', 'm', 'k', and 'friendships' will hold the values from the last iteration of the loop. The values of 't' and 'stdin' remain unchanged.

#Overall this is what the function does:This function accepts four parameters: a positive integer n, a non-negative integer m, a positive integer k, and a list of m lists representing friendships. It processes the input data and returns a result, which is then printed to the console. The function's purpose is to analyze the friendships data and produce an output based on the values of n, m, and k. After the function concludes, the program state is updated with the result of the function call, and the input variables n, m, k, and friendships hold their respective values from the last iteration of the loop.

