#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case consists of an integer n (1 <= n <= 2 * 10^5) followed by n non-negative integers (0 <= a_j < 2^31). The sum of n over all test cases does not exceed 2 * 10^5.
    times = int(input())
    check = 2 ** 31 - 1
    for _ in range(times):
        n = int(input())
        
        data = list(map(int, input().split()))
        
        dic = dict()
        
        ans = n
        
        check = 2 ** 31 - 1
        
        for i in data:
            s = i ^ check
            if s in dic:
                dic[s] -= 1
                ans -= 1
                if dic[s] == 0:
                    del dic[s]
            elif i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
            print(ans)
        
    #State: Output State: The loop has executed 'times' iterations, and for each iteration, it has read 'n' integers from the standard input, processed them, and printed the result. The value of 'check' remains unchanged at 2147483647. The loop has finished executing, and the program has terminated.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer n followed by n non-negative integers. For each test case, it processes the integers by performing bitwise XOR operations with a predefined value (2^31 - 1), and maintains a dictionary to keep track of the counts of these XOR results. The function then prints the number of integers that do not have a corresponding XOR pair in the dictionary. The function repeats this process for the specified number of test cases, and then terminates.

