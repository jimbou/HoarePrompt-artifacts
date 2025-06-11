#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains a single integer t (1 <= t <= 1000) — the number of test cases. Each of the following t lines contains two integers n and k (2 <= n <= 10^8, 1 <= k <= 4n - 2) — the size of the square grid and the minimum number of diagonals in which there should be at least one colored cell.
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        
        if k % 2 == 0 and k // 2 % 2 == 1:
            print(k // 2 + 1)
        else:
            print(ceil(k / 2))
        
    #State: Output State: The output state will be a series of integers, each on a new line, representing the minimum number of colored cells required for each test case. The number of lines in the output will be equal to the value of `t`. The value of `t` remains unchanged, and the contents of stdin will be consumed by the loop.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of two integers: the size of a square grid and the minimum number of diagonals that should contain at least one colored cell. It then calculates and prints the minimum number of colored cells required for each test case, with the output being a series of integers, one per test case. The function consumes the contents of standard input and leaves the value of the number of test cases unchanged.

