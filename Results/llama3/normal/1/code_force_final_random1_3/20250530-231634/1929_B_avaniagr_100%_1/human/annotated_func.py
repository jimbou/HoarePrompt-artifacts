#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains an integer t (1 <= t <= 1000). Each of the following t lines contains two integers n and k (2 <= n <= 10^8, 1 <= k <= 4n - 2).
    for s in [*open(0)][1:]:
        n, k = map(int, s.split())
        
        if k <= 4 * n - 4:
            print(math.ceil(k / 2))
        elif k == 4 * n - 3:
            print(2 * n - 1)
        elif k == 4 * n - 2:
            print(2 * n)
        
    #State: The loop has finished executing, and the output state is the same as the initial state, with the addition of the output values printed during the loop's execution.

#Overall this is what the function does:The function reads input from stdin, expecting multiple lines of input where the first line contains an integer t, and each subsequent line contains two integers n and k. It then processes each pair of n and k, and based on the value of k relative to n, it prints a calculated value. The function does not modify the input state and only appends the calculated output values to the output state.

