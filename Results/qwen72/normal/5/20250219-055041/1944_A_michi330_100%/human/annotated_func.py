#State of the program right berfore the function call: The function `func` is expected to take two parameters, `n` and `k`, where `n` is an integer representing the number of islands (1 ≤ n ≤ 100), and `k` is an integer representing the maximum number of bridges Dominater can destroy (0 ≤ k ≤ n(n - 1)/2). The function should be called within a loop that processes multiple test cases, where the number of test cases `t` is an integer (1 ≤ t ≤ 10^3).
def func():
    t = int(input())
    for i in range(0, t, 1):
        n, k = map(int, input().split())
        
        if k >= n - 1:
            print(1)
        else:
            print(n)
        
    #State: `t` is an input integer (1 ≤ t ≤ 10^3), `i` is `t`, `n` and `k` are input integers. The values of `t`, `i`, `n`, and `k` remain unchanged after the loop completes all iterations.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, representing the number of test cases (1 ≤ t ≤ 10^3). For each test case, it reads two integers `n` and `k` from the input, where `n` is the number of islands (1 ≤ n ≤ 100) and `k` is the maximum number of bridges that can be destroyed (0 ≤ k ≤ n(n - 1)/2). If `k` is greater than or equal to `n - 1`, the function prints `1`. Otherwise, it prints `n`. After processing all test cases, the function does not return any value, and the variables `t`, `i`, `n`, and `k` are no longer in scope.

