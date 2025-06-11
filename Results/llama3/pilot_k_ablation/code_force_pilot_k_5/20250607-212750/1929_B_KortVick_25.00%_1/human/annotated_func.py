#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains a single integer t (1 <= t <= 1000) — the number of test cases. Each of the following t lines contains two integers n and k (2 <= n <= 10^8, 1 <= k <= 4n - 2) — the size of the square grid and the minimum number of diagonals in which there should be at least one colored cell.
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        
        if k % 2 == 0 and k // 2 % 2 == 1:
            print(k // 2 + 1)
        else:
            print(ceil(k / 2))
        
    #State: `t` is 0, `n` is an integer between 2 and 10^8 (inclusive), `k` is an integer between 1 and 4n - 2 (inclusive), stdin is empty.

#Overall this is what the function does:The function reads a series of test cases from standard input, where each test case consists of a square grid size (n) and a minimum number of diagonals (k) that should have at least one colored cell. It then calculates and prints the minimum number of cells that need to be colored to meet the condition for each test case, based on whether k is even or odd. The function processes all test cases and empties the standard input.

