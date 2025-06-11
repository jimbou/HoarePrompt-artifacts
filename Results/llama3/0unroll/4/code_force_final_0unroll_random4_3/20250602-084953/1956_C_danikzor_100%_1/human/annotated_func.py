#State of the program right berfore the function call: stdin contains multiple test cases. The first line contains the number of test cases t (1 <= t <= 500). Each test case contains a single integer n (1 <= n <= 500) — the size of the matrix a.
    n = int(input())
    print(n * (n + 1) * (4 * n - 1) // 6, 2 * n)
    #This is printed: the sum of squares of the first n natural numbers, twice the value of n (where n is an integer between 1 and 500 inclusive)
    for i in range(1, n + 1):
        print(1, i, *range(n, 0, -1))
        
        print(2, i, *range(n, 0, -1))
        
    #State: The value of the formula n * (n + 1) * (4 * n - 1) // 6 and the value of 2 * n, followed by 2 * n lines of output, each containing the numbers 1 or 2, the current value of i, and the numbers from n down to 1.

#Overall this is what the function does:The function reads an integer n from standard input, calculates and prints the sum of squares of the first n natural numbers and twice the value of n, then generates and prints 2n lines of output, each containing the numbers 1 or 2, the current value of i, and the numbers from n down to 1, for i ranging from 1 to n.

