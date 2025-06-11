#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains a single integer t (1 <= t <= 1000) — the number of test cases. Each of the following t lines contains two integers n and k (2 <= n <= 10^8, 1 <= k <= 4n - 2) — the size of the square grid and the minimum number of diagonals in which there should be at least one colored cell.
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        
        if 4 * n - 2 == k:
            print(k // 2 + 1)
        else:
            print(ceil(k / 2))
        
    #State: The loop has executed t times, and for each iteration, it has printed either k // 2 + 1 or ceil(k / 2) to the console, depending on the condition 4 * n - 2 == k. The values of t, n, and k have been updated accordingly in each iteration. The stdin has been consumed by t lines of input.

#Overall this is what the function does:The function reads a series of test cases from standard input, where each test case consists of two integers: the size of a square grid (n) and the minimum number of diagonals that should contain at least one colored cell (k). For each test case, it prints the minimum number of cells that need to be colored to meet the condition. If the minimum number of diagonals is equal to 4n - 2, it prints k // 2 + 1; otherwise, it prints ceil(k / 2). The function processes all test cases and prints the results to the console.

