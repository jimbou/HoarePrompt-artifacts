#State of the program right berfore the function call: stdin contains multiple test cases. The first line contains the number of test cases t (1 <= t <= 500). Each test case contains a single integer n (1 <= n <= 500) — the size of the matrix a.
    n = int(input())
    print(n * (n + 1) * (4 * n - 1) // 6, 2 * n)
    #This is printed: the sum of the squares of the first n positive integers, 2n (where n is an integer between 1 and 500)
    for i in range(1, n + 1):
        print(1, i, *range(n, 0, -1))
        
        print(2, i, *range(n, 0, -1))
        
    #State: `n` is an integer between 1 and 500 (inclusive), stdin contains multiple test cases (t-n test cases remaining), `i` is `n`, and this is printed: "2, `n`, and the numbers from `n` down to 1 in reverse order"

#Overall this is what the function does:The function reads an integer n from standard input, representing the size of a matrix, and prints the sum of the squares of the first n positive integers and 2n. It then prints 2n lines, each containing the numbers from 1 to n and from n down to 1 in reverse order, with the first two numbers being 1 and 2, respectively. The function leaves the state of the program with n being an integer between 1 and 500 (inclusive) and standard input containing multiple test cases (t-n test cases remaining).

