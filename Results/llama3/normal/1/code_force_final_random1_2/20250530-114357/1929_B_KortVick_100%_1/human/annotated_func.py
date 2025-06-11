#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains a single integer t (1 <= t <= 1000) — the number of test cases. Each of the following t lines contains two integers n and k (2 <= n <= 10^8, 1 <= k <= 4n - 2) — the size of the square grid and the minimum number of diagonals in which there should be at least one colored cell.
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        
        if 4 * n - 2 == k:
            print(k // 2 + 1)
        else:
            print(ceil(k / 2))
        
    #State: `t` is an integer between 0 and 997 (inclusive), `n` is an integer, `k` is an integer, `_` is `t`, and stdin is empty. If `4 * n - 2` equals `k`, the integer division of `k` by 2 plus 1 is printed. Otherwise, the ceiling of `k` divided by 2 is printed.

#Overall this is what the function does:The function reads a series of test cases from standard input, where each case consists of a square grid size (n) and a minimum number of diagonals (k) that should contain at least one colored cell. For each test case, it prints the minimum number of cells that need to be colored to meet the condition. If the minimum number of diagonals is equal to the maximum possible (4n - 2), it prints half of this number plus one; otherwise, it prints the ceiling of half of the minimum number of diagonals. The function processes all test cases and then terminates, leaving the standard input empty.

