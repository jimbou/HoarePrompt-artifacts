#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two space-separated integers: n and k, where n is an integer between 2 and 10^8 (inclusive) and k is an integer between 1 and 4n - 2 (inclusive).
    for _ in range(int(input())):
        n, k = map(int, input().split())
        
        if k == 1:
            print(1)
            continue
        
        if k <= 2 * n:
            print(math.ceil(k / 2))
        else:
            print(k // 2 + 1)
        
    #State: The output state will contain multiple lines, each containing a single integer. The integer on each line will be the result of the calculation for the corresponding test case. Specifically, for each test case, if k is 1, the output will be 1. If k is less than or equal to 2n, the output will be the ceiling of k divided by 2. If k is greater than 2n, the output will be k divided by 2 plus 1.

#Overall this is what the function does:Calculates and prints the result of a mathematical operation for multiple test cases, where each test case consists of two integers, n and k. For each test case, if k is 1, the result is 1. If k is less than or equal to 2n, the result is the ceiling of k divided by 2. If k is greater than 2n, the result is k divided by 2 plus 1. The results are printed on separate lines for each test case.

