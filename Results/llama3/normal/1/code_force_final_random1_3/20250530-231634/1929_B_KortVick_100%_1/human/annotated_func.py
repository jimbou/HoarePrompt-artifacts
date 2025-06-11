#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains an integer t (1 <= t <= 1000) representing the number of test cases. Each of the following t lines contains two integers n and k (2 <= n <= 10^8, 1 <= k <= 4n - 2) representing the size of the square grid and the minimum number of diagonals in which there should be at least one colored cell.
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        
        if 4 * n - 2 == k:
            print(k // 2 + 1)
        else:
            print(ceil(k / 2))
        
    #State: `t` is an integer between 1 and 1000, stdin contains multiple lines of input, each containing two integers `n` and `k` (2 <= n <= 10^8, 1 <= k <= 4n - 2), where `n` represents the size of the square grid and `k` represents the minimum number of diagonals in which there should be at least one colored cell.

#Overall this is what the function does:This function reads input from stdin, processes multiple test cases, and prints the minimum number of cells that need to be colored in a square grid of size n to have at least one colored cell in k diagonals. The function takes no parameters and returns no value, but it prints the result for each test case.

