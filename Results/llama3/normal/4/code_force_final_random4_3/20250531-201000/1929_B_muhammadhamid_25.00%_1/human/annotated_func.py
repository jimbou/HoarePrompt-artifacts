#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains a single integer t (1 <= t <= 1000) — the number of test cases. Each of the following t lines contains two integers n and k (2 <= n <= 10^8, 1 <= k <= 4n - 2) — the size of the square grid and the minimum number of diagonals in which there should be at least one colored cell.
    for _ in range(int(input())):
        n, k = map(int, input().split())
        
        if k == 1:
            print(1)
            continue
        
        if k <= 2 * n:
            print(math.ceil(k / 2))
        else:
            print(k // 2 + 1)
        
    #State: The loop has executed for the number of times specified by the integer t in the first line of stdin. For each iteration, if k is 1, the number 1 is printed and the rest of the code inside the current loop is skipped, moving to the next iteration. Otherwise, if k is less than or equal to twice the value of n, the ceiling of half of k is printed. If k is larger than twice the value of n, the value of k // 2 + 1 is printed.

#Overall this is what the function does:This function reads a number of test cases from standard input, then for each test case, it reads the size of a square grid and the minimum number of diagonals that should have at least one colored cell. It prints the minimum number of cells that need to be colored to meet the diagonal requirement. If the minimum number of diagonals is 1, it prints 1. If the minimum number of diagonals is less than or equal to twice the grid size, it prints the ceiling of half the minimum number of diagonals. Otherwise, it prints half the minimum number of diagonals plus 1.

