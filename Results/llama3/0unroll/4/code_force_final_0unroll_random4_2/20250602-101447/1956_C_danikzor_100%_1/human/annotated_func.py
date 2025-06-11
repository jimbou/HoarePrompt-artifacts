#State of the program right berfore the function call: stdin contains multiple test cases. The first line contains the number of test cases t (1 <= t <= 500). Each test case contains a single integer n (1 <= n <= 500) — the size of the matrix a.
    n = int(input())
    print(n * (n + 1) * (4 * n - 1) // 6, 2 * n)
    #This is printed: the sum of squares of the first n natural numbers, twice the value of n (where n is an integer between 1 and 500 inclusive)
    for i in range(1, n + 1):
        print(1, i, *range(n, 0, -1))
        
        print(2, i, *range(n, 0, -1))
        
    #State: The output state after the loop executes all the iterations is that the product of `n`, `n+1`, and `4*n-1` divided by 6, and 2 times `n` have been printed to the console, and the values of `i` and `n` remain unchanged. The loop has iterated `n` times, printing the values of `i` and the range from `n` to 1 in reverse order, twice for each iteration.

#Overall this is what the function does:The function reads an integer n from standard input, representing the size of a matrix, and prints the sum of squares of the first n natural numbers and twice the value of n. It then iterates n times, printing the values of i and the range from n to 1 in reverse order, twice for each iteration. The function does not return any value, only producing output to the console.

