#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains an integer t (1 <= t <= 1000) — the number of test cases. Each of the following t lines contains two integers n and k (2 <= n <= 10^8, 1 <= k <= 4n - 2) — the size of the square grid and the minimum number of diagonals in which there should be at least one colored cell.
    for _ in range(int(input())):
        n, k = map(int, input().split())
        
        if k == 1:
            print(1)
            continue
        
        if k <= 2 * n:
            print(math.ceil(k / 2))
        else:
            print(k // 2 + 1)
        
    #State: The output state contains multiple lines of output. The number of lines is equal to the number of test cases t. Each line contains an integer representing the minimum number of cells that need to be colored to satisfy the condition for the corresponding test case.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of a square grid size (n) and a minimum number of diagonals (k) that should have at least one colored cell. It then calculates and prints the minimum number of cells that need to be colored to satisfy the condition for each test case. The output is a series of integers, one for each test case, representing the minimum number of cells to be colored.

