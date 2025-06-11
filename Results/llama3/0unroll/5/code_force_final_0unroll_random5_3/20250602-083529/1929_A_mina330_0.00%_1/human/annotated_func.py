#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer (the number of elements in the list) and then a list of integers. The integer is a non-negative integer and less or equal than 100. The integers in the list are between 1 and 10^9.
    ntest = int(input())
    for itest in range(0, ntest, 1):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        a.sort()
        
        kq = 0
        
        for i in range(0, len(a) // 2, 1):
            kq = kq + a[len(a) - i - 1] - a[i]
        
        print(kq)
        
    #State: Output State: The output state will be the sum of the differences between the largest and smallest numbers in each test case, repeated for the number of test cases specified by `ntest`.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer (the number of elements in the list) followed by a list of integers. It sorts each list in ascending order, then calculates the sum of the differences between the largest and smallest numbers in each list, repeating this process for the specified number of test cases. The function outputs the calculated sums for each test case.

