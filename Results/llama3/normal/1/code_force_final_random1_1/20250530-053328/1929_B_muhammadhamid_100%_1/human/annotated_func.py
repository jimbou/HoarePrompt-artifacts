#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two integers n and k, where n is a positive integer greater than or equal to 2 and k is a positive integer greater than or equal to 1 and less than or equal to 4n - 2.
    for _ in range(int(input())):
        n, k = map(int, input().split())
        
        if k == 1:
            print(1)
            continue
        
        if k <= 2 * (n + (n - 2)):
            print(math.ceil(k / 2))
        else:
            print(k // 2 + 1)
        
    #State: _ is the number of test cases minus 1, `n` is an integer at least 2, `k` is an integer, stdin contains no more input. If `k` is 1, the number 1 is printed and we skip to the next iteration of the loop. If `k` is less than or equal to 2 times the value of `n` plus `n` minus 2, the ceiling of `k` divided by 2 is printed. Otherwise, the integer division of `k` by 2 plus 1 is printed.

#Overall this is what the function does:The function processes multiple test cases from standard input, where each test case consists of two integers, n and k. For each test case, it prints a calculated value based on the values of n and k. If k is 1, it prints 1. If k is less than or equal to 2 times the value of n plus n minus 2, it prints the ceiling of k divided by 2. Otherwise, it prints the integer division of k by 2 plus 1. After processing all test cases, the function leaves the standard input empty.

