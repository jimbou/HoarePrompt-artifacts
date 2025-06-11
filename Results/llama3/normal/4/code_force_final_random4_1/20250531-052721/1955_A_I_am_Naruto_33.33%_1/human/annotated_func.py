#State of the program right berfore the function call: stdin contains t+1 inputs: first an integer t (1 <= t <= 10^4) and then t sets of three integers n, a, and b (1 <= n <= 100, 1 <= a, b <= 30).
    for _ in range(int(input())):
        n, a, b = map(int, input().split())
        
        if n > 1:
            ans1 = a * n
            ans2 = b * n // 2 + a * n % 2
            print(min(ans1, ans2))
        else:
            print(a)
        
    #State: The loop iterates t times, and for each iteration, if n > 1, the minimum of a * n and b * n // 2 + a * n % 2 is printed. If n is 1, the value of a is printed. After all iterations, the loop finishes executing.

#Overall this is what the function does:The function reads a series of inputs from standard input, where the first input is an integer t representing the number of test cases, followed by t sets of three integers n, a, and b. For each test case, if n is greater than 1, it calculates and prints the minimum of two values: a multiplied by n, and b multiplied by n divided by 2 plus a multiplied by n modulo 2. If n is 1, it simply prints the value of a. The function iterates this process t times, printing the results for each test case.

