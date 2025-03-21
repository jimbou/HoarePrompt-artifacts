#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5⋅10^4. For each test case, n, m, and k are integers such that 2 ≤ n ≤ 10^5, 0 ≤ m ≤ min(10^5, n(n-1)/2), and 1 ≤ k ≤ 2⋅10^5. Each of the next m lines contains three integers a_i, b_i, and f_i such that a_i ≠ b_i, 1 ≤ a_i, b_i ≤ n, and 1 ≤ f_i ≤ 10^9. It is guaranteed that all pairs of friends are distinct, and the sum of n and the sum of m over all test cases does not exceed 10^5, and the sum of k over all test cases does not exceed 2⋅10^5.
def func():
    t = int(input())
    M = 10 ** 9 + 7
    for i in range(t):
        n, m, k = map(int, input().split())
        
        sum_f = 0
        
        for j in range(m):
            a, b, f = map(int, input().split())
            sum_f += f
        
        cn2 = n * (n - 1) // 2
        
        p = 2 * k * cn2 * sum_f + m * k * (k - 1)
        
        q = 2 * cn2 ** 2
        
        gcd = math.gcd(p, q)
        
        p = p // gcd
        
        q = q // gcd
        
        print(int(p * pow(q, -1, M) % M))
        
    #State: Output State: The output state will consist of a series of integers, each representing the result of the expression `(p * pow(q, -1, M) % M)` for each iteration of the outer loop. Each value of `p` and `q` is derived from the inputs provided in each iteration of the inner loop, and the greatest common divisor (gcd) operation is used to simplify the fraction before performing the modular inverse and final modulo operation with `M`.
    #
    #Each line of output will contain one such result, corresponding to one complete set of inputs provided by the `input()` function calls within the loop. The number of lines in the output will be equal to the value of `t`, which is the number of times the outer loop runs.
#Overall this is what the function does:The function processes multiple test cases, where each test case involves integers \( t \), \( n \), \( m \), and \( k \), along with a list of friend pairs \((a_i, b_i, f_i)\). For each test case, it calculates a specific mathematical expression involving these inputs, simplifies the result using the greatest common divisor (gcd), and then computes the modular inverse and final result modulo \( M \). The function outputs a series of integers, each corresponding to the calculated result for each test case.

