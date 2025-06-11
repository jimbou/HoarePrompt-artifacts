#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer and then a list of integers. The integer is a positive integer (1 <= n <= 2 * 10^5). The list of integers is of length n and contains non-negative integers less than n. The sum of n over all test cases does not exceed 2 * 10^5.
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
                    c -= 1
                    if not c or j == n:
                        print(j)
                        break
        
    #State: The output state is a list of integers, where each integer represents the smallest index j such that the count of j in the input list a is less than 2, or 0 if no such index exists. The list has the same number of elements as the number of test cases in the input.

#Overall this is what the function does:This function processes multiple test cases from standard input, where each test case consists of a positive integer n and a list of n non-negative integers less than n. It calculates the smallest index j such that the count of j in the input list is less than 2, or 0 if no such index exists, and prints this value for each test case.

