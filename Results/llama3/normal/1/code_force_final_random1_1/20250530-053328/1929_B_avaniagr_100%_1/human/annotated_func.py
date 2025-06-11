#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains a single integer t (1 <= t <= 1000) — the number of test cases. Each of the following t lines contains two integers n and k (2 <= n <= 10^8, 1 <= k <= 4n - 2) — the size of the square grid and the minimum number of diagonals in which there should be at least one colored cell.
    for s in [*open(0)][1:]:
        n, k = map(int, s.split())
        
        if k <= 4 * n - 4:
            print(math.ceil(k / 2))
        elif k == 4 * n - 3:
            print(2 * n - 1)
        elif k == 4 * n - 2:
            print(2 * n)
        
    #State: The loop has executed for all the iterations, and the output state is the same as the initial state, with the addition of the output of the loop for each iteration.

#Overall this is what the function does:This function reads input from standard input, processes multiple test cases, and prints the minimum number of colored cells required to have at least one colored cell in a specified number of diagonals in a square grid. The function takes no arguments and returns no value, instead, it prints the results for each test case.

