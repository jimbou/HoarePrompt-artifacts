#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains a single integer t (1 <= t <= 1000) — the number of test cases. Each of the following t lines contains two integers n and k (2 <= n <= 10^8, 1 <= k <= 4n - 2) — the size of the square grid and the minimum number of diagonals in which there should be at least one colored cell.
    for s in [*open(0)][1:]:
        n, k = map(int, s.split())
        
        if k <= 4 * n - 4:
            print(math.ceil(k / 2))
        elif k == 4 * n - 3:
            print(2 * n - 1)
        elif k == 4 * n - 2:
            print(2 * n)
        
    #State: The output state will contain t lines, each containing a single integer. The integer on each line represents the minimum number of colored cells required to satisfy the condition for the corresponding test case.

#Overall this is what the function does:This function reads multiple lines of input from stdin, where the first line contains the number of test cases, and each subsequent line contains two integers representing the size of a square grid and the minimum number of diagonals with at least one colored cell. It then calculates and prints the minimum number of colored cells required to satisfy the condition for each test case, based on the given grid size and diagonal requirements.

