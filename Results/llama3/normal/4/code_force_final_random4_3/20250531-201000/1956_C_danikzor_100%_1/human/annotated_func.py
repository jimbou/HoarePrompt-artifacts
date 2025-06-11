#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains one integer n (1 <= n <= 500).
    n = int(input())
    print(n * (n + 1) * (4 * n - 1) // 6, 2 * n)
    #This is printed: the sum of the squares of the first n odd numbers, 2 times n (where n is an integer between 1 and 500 inclusive)
    for i in range(1, n + 1):
        print(1, i, *range(n, 0, -1))
        
        print(2, i, *range(n, 0, -1))
        
    #State: `n` is an integer between 1 and 500 (inclusive), stdin contains multiple test cases minus one test case, this is printed: the value of the expression `n * (n + 1) * (4 * n - 1) // 6` and the value of the expression `2 * n`, `i` is `n`,  `n` must be greater than or equal to 0, and this is printed: 1, the value of `i` which is `n`, and the values of the range from `n` down to 1 in reverse order (exclusive of 0), where `n` is an integer between 1 and 500 (inclusive), and this is printed: 2, the value of `i` which is `n`, and the values of the range from `n` down to 1 in reverse order (exclusive of 0).

#Overall this is what the function does:The function reads an integer n from standard input, where n is between 1 and 500 (inclusive), and prints the sum of the squares of the first n odd numbers and 2 times n. Then, for each number i from 1 to n, it prints two lines: one starting with 1, followed by i and the numbers from n down to 1 in reverse order (exclusive of 0), and another starting with 2, followed by i and the same sequence of numbers. After processing, the function leaves the input stream with one fewer test case.

