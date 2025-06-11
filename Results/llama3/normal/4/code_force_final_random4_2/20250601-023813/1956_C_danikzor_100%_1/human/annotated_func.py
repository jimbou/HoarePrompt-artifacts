#State of the program right berfore the function call: stdin contains multiple test cases. The first line contains the number of test cases t (1 <= t <= 500). Each test case contains a single integer n (1 <= n <= 500) — the size of the matrix a.
    n = int(input())
    print(n * (n + 1) * (4 * n - 1) // 6, 2 * n)
    #This is printed: sum of squares of the first n natural numbers, 2n (where n is an integer between 1 and 500 inclusive)
    for i in range(1, n + 1):
        print(1, i, *range(n, 0, -1))
        
        print(2, i, *range(n, 0, -1))
        
    #State: `n` is greater than or equal to 1, `i` is `n`, stdin contains multiple test cases minus one, and the following is printed: 2, the value of `i` which is `n`, and the numbers from `n` down to 1 in reverse order

#Overall this is what the function does:This function reads the number of test cases and the size of a matrix from standard input, calculates and prints the sum of squares of the first n natural numbers and 2n, and then prints a specific pattern of numbers for each test case. The function iterates through each test case, printing the calculated values and the pattern of numbers, until all test cases have been processed.

