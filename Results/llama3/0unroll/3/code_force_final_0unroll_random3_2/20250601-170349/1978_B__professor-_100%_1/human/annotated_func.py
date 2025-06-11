#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains a single integer t (1 <= t <= 10^4). Each of the following t lines contains three integers n, a, and b (1 <= n, a, b <= 10^9).
    t = int(input())
    for _ in range(t):
        n, a, b = map(int, input().split())
        
        if b <= a:
            print(n * a)
        elif b - a >= n:
            print(int((2 * b - n + 1) * n // 2))
        else:
            print(int((b - a) * (b - a + 1) // 2 + a * n))
        
    #State: The output will be t lines, each containing the maximum sum of n numbers in an arithmetic sequence with the first term a and the common difference b.

#Overall this is what the function does:This function reads input from stdin, processes it, and prints the maximum sum of n numbers in an arithmetic sequence with the first term a and the common difference b for each test case. It takes no arguments and returns no value, instead printing the results directly to stdout. The function handles multiple test cases, each with its own set of input values for n, a, and b.

