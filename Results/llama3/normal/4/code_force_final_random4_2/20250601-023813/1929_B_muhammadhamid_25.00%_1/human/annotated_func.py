#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two integers: n and k, where n is a positive integer and k is a positive integer such that 1 <= k <= 4n - 2.
    for _ in range(int(input())):
        n, k = map(int, input().split())
        
        if k == 1:
            print(1)
            continue
        
        if k <= 2 * n:
            print(math.ceil(k / 2))
        else:
            print(k // 2 + 1)
        
    #State: _ is the number of test cases minus 1, `n` is an integer, `k` is an integer, and stdin contains no more test cases. If `k` is 1, the number 1 is printed and the current iteration of the loop is skipped, moving on to the next iteration. Otherwise, if `k` is less than or equal to twice `n`, the ceiling of the division of `k` by 2 is printed. If `k` is greater than twice `n`, the integer division of `k` by 2 plus 1 is printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two positive integers, n and k. For each test case, it prints a value based on the relationship between k and n: if k is 1, it prints 1; if k is less than or equal to 2n, it prints the ceiling of k divided by 2; otherwise, it prints k divided by 2 plus 1. After processing all test cases, the function leaves the standard input empty.

