#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two integers: n and k, where n is a positive integer and k is an integer such that 1 <= k <= 4n - 2.
    for _ in range(int(input())):
        n, k = map(int, input().split())
        
        if k == 1:
            print(1)
            continue
        
        if k <= 2 * (n + (n - 2)):
            print(math.ceil(k / 2))
        else:
            print(k // 2 + 1)
        
    #State: All test cases have been processed and their corresponding outputs have been printed.

#Overall this is what the function does:This function processes multiple test cases from standard input, where each test case contains two integers, n and k. It calculates and prints the corresponding output for each test case based on the value of k, either printing 1, the ceiling of k divided by 2, or k divided by 2 plus 1. After processing all test cases, the function concludes, having printed the outputs for all cases.

