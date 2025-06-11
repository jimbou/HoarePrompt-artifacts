#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three integers k, x and a, where k is an integer between 2 and 30, x is an integer between 1 and 100, and a is an integer between 1 and 10^9.
    for _ in range(int(input())):
        k, x, a = map(int, input().split())
        
        s = 1
        
        for i in range(x):
            s += s // (k - 1) + 1
        
        print('YES' if a >= s else 'NO')
        
    #State: stdin is empty, k, x, and a are integers, s is 1 plus x times the integer division of s by k-1 plus x, i is -1, _ is the number of test cases, and it is printed whether a is greater than or equal to s or not for each test case.

#Overall this is what the function does:This function processes multiple test cases from standard input, where each test case consists of three integers: k, x, and a. It calculates a value s based on k and x, and then prints 'YES' if a is greater than or equal to s, and 'NO' otherwise. The function continues this process until all test cases have been processed, leaving the standard input empty.

