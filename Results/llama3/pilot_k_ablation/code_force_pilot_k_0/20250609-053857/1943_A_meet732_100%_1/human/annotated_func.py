#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer and then a list of integers. The first integer is a positive integer (1 <= n <= 2 * 10^5). The second input is a list of n non-negative integers (0 <= a_i < n). The sum of n over all test cases does not exceed 2 * 10^5.
    for _ in range(int(input())):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        cntl = [(0) for _ in range(n + 1)]
        
        for i in a:
            cntl[i] += 1
        
        if cntl[0] == 0:
            print(0)
        else:
            c = min(2, cntl[0])
            for j in range(1, n + 1):
                if cntl[j] < 2:
                    if cntl[j] == 0:
                        print(j)
                        break
                    else:
                        c -= 1
                        if not c:
                            print(j)
                            break
        
    #State: The output state will be a list of integers, each representing the smallest index j such that the count of j in the list a is less than 2. If no such index is found, the output will be 0. The list will have the same number of elements as the number of test cases in the input.

#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of a positive integer n and a list of n non-negative integers. It then finds the smallest index j such that the count of j in the list is less than 2. If no such index is found, it outputs 0. The function repeats this process for each test case and outputs a list of integers, each representing the smallest index j for the corresponding test case.

