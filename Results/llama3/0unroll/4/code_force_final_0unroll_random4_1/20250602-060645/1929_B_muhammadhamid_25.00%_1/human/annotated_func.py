#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two integers n and k such that 2 <= n <= 10^8 and 1 <= k <= 4n - 2.
    for _ in range(int(input())):
        n, k = map(int, input().split())
        
        if k == 1:
            print(1)
            continue
        
        if k <= 2 * n:
            print(math.ceil(k / 2))
        else:
            print(k // 2 + 1)
        
    #State: The output state will contain the results of the calculations for each test case, where each result is the minimum number of operations required to make all elements of the array equal. The results will be printed on separate lines, in the order they were received as input.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two integers n and k. It calculates and prints the minimum number of operations required to make all elements of an array equal, based on the values of n and k. The function handles three cases: when k is 1, when k is less than or equal to 2n, and when k is greater than 2n. For each test case, it prints the calculated result on a separate line.

