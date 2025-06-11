#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains a single integer t (1 <= t <= 1000) — the number of test cases. Each of the following t lines contains two integers n and k (2 <= n <= 10^8, 1 <= k <= 4n - 2) — the size of the square grid and the minimum number of diagonals in which there should be at least one colored cell.
    for _ in range(int(input())):
        n, k = map(int, input().split())
        
        if k == 1:
            print(1)
            continue
        
        if k <= 2 * (n + (n - 2)):
            print(math.ceil(k / 2))
        else:
            print(k // 2 + 1)
        
    #State: The output state will be the result of t executions of the loop, where each execution will print the minimum number of colored cells required to satisfy the condition for the given n and k values. The output will be a series of integers, one for each test case, representing the minimum number of colored cells required.

#Overall this is what the function does:The function reads multiple lines of input from stdin, where the first line contains the number of test cases (t) and each subsequent line contains two integers (n and k) representing the size of a square grid and the minimum number of diagonals with at least one colored cell, respectively. It then processes each test case, printing the minimum number of colored cells required to satisfy the condition for the given n and k values. The output is a series of integers, one for each test case, representing the minimum number of colored cells required.

