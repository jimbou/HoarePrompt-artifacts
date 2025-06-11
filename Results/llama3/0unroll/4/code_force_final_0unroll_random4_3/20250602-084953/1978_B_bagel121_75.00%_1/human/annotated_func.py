#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three integers n, a, and b (1 <= n, a, b <= 10^9).
    t = int(input())
    for _ in range(t):
        n, a, b = map(int, input().split())
        
        if a >= b:
            print(n * a)
        else:
            k = min(b - a + 1, n)
            ans = int((b + (b - k + 1)) / 2 * k)
            p2 = (n - k) * a
            print(ans + p2)
        
    #State: The output state is a series of integers, each representing the maximum sum that can be obtained from a test case. The number of integers in the output state is equal to the value of `t`, which is the number of test cases. Each integer is calculated based on the values of `n`, `a`, and `b` in each test case, using the formula `n * a` if `a` is greater than or equal to `b`, or `(b + (b - k + 1)) / 2 * k + (n - k) * a` if `a` is less than `b`, where `k` is the minimum of `b - a + 1` and `n`.

#Overall this is what the function does:This function reads multiple test cases from standard input, each containing three integers n, a, and b. For each test case, it calculates and prints the maximum sum that can be obtained based on the values of n, a, and b. If a is greater than or equal to b, the maximum sum is n * a. Otherwise, the maximum sum is calculated using the formula (b + (b - k + 1)) / 2 * k + (n - k) * a, where k is the minimum of b - a + 1 and n. The function outputs a series of integers, each representing the maximum sum for a test case, with the number of integers equal to the number of test cases.

