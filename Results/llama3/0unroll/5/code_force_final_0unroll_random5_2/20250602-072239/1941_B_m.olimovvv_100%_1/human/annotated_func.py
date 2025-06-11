#State of the program right berfore the function call: stdin contains multiple inputs: first an integer t, then for each test case, first an integer n and then a list of n integers.
    for _ in range(int(input())):
        a = int(input())
        
        b = list(map(int, input().split()))
        
        for i in range(0, a - 2):
            if b[i] < 0:
                print('NO')
                break
            b[i + 1] -= b[i] * 2
            b[i + 2] -= b[i]
            b[i] -= b[i]
        else:
            if b[-1] != 0 or b[-2] != 0:
                print('NO')
            else:
                print('YES')
        
    #State: The output state will be a series of 'YES' or 'NO' printed to the console, depending on whether the list of integers can be reduced to zero by the given operations. The number of 'YES' or 'NO' will be equal to the number of test cases (t). The stdin will be empty after all inputs have been read.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer n followed by a list of n integers. It then attempts to reduce the list of integers to zero by iteratively applying a set of operations (subtracting twice the current element from the next element, subtracting the current element from the element after next, and setting the current element to zero). If the list can be reduced to zero, it prints 'YES' to the console; otherwise, it prints 'NO'. The function repeats this process for each test case, printing a series of 'YES' or 'NO' outputs equal to the number of test cases.

