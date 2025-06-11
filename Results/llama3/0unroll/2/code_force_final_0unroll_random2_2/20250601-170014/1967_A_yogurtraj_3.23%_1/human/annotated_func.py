#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line contains two integers n and k, where n is a positive integer and k is a non-negative integer. The second line contains n integers a_1, a_2, ..., a_n, where each a_i is a positive integer.
    for ii in range(int(input())):
        n, k = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        a.sort()
        
        r = a[0]
        
        rem = 0
        
        y = 0
        
        for i in range(0, n - 1):
            if (i + 1) * (a[i + 1] - a[i]) > k:
                r = a[i] + k // (i + 1)
                rem = k % (i + 1)
                y = n - 1 - i
                k = 0
                break
            else:
                k -= (i + 1) * (a[i + 1] - a[i])
                r = a[i + 1]
        
        if k != 0:
            r = a[n - 1] + k // n
            print((r - 1) * n + 1)
        else:
            print((r - 1) * n + 1 + rem + y)
        
    #State: The output state will be a series of numbers, each representing the result of a test case. Each result is calculated based on the input values of n, k, and the list of integers a. The result is determined by the loop's execution, which sorts the list a, calculates the value of r, and then prints the result based on the values of r, k, and n. The output state will contain one result for each test case in the input.

#Overall this is what the function does:This function processes multiple test cases from standard input, where each test case consists of two lines: the first line contains two integers n and k, and the second line contains n positive integers. The function sorts the integers, calculates a value r based on the sorted list and k, and then prints a result for each test case. The result is determined by the value of r, k, and n, and is calculated differently depending on whether k is zero or non-zero. The function outputs a series of numbers, each representing the result of a test case.

