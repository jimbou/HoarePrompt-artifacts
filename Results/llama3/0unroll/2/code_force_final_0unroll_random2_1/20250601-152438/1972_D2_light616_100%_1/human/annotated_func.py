#State of the program right berfore the function call: n and m are positive integers such that 1 <= n, m <= 2 * 10^6.
    x = 1
    cnt = 0
    n, m = map(int, input().split())
    while x * x <= n:
        y = 1
        
        while (x + y) * x <= n and (x + y) * y <= m:
            if math.gcd(x, y) == 1:
                cnt += min(n // ((x + y) * x), m // ((x + y) * y))
            y += 1
        
        x += 1
        
    #State: cnt is the number of coprime pairs (a, b) such that 1 <= a <= n, 1 <= b <= m, and gcd(a, b) = 1.
    print(cnt)
    #This is printed: cnt (where cnt is the number of coprime pairs (a, b) such that 1 <= a <= n, 1 <= b <= m, and gcd(a, b) = 1)

#Overall this is what the function does:This function calculates and prints the number of coprime pairs (a, b) such that 1 <= a <= n and 1 <= b <= m, where n and m are positive integers provided as input, and gcd(a, b) = 1.

#State of the program right berfore the function call: stdin contains an integer t (1 ≤ t ≤ 10^4) followed by t lines, each containing two positive integers n and m (1 ≤ n, m ≤ 2 * 10^6).
    t = int(input())
    for _ in range(t):
        func_1()
        
    #State: The loop will execute `t` times, and after each execution, the function `func_1()` will be called. The state of `t` will be decremented by 1 after each iteration, and the state of the variables inside `func_1()` will be updated accordingly. After the loop finishes, `t` will be 0, and the state of the variables inside `func_1()` will be the state after the last execution of `func_1()`. The state of `n` and `m` will remain unchanged as they are not affected by the loop head and body.

#Overall this is what the function does:The function reads an integer `t` from standard input, representing the number of test cases, and then iterates `t` times. In each iteration, it calls the function `func_1()`, which is not defined in the provided code snippet. The function does not return any value or modify any external state, but it may have side effects through the execution of `func_1()`. After the loop finishes, the function terminates, leaving the state of the variables inside `func_1()` as they were after the last execution.

