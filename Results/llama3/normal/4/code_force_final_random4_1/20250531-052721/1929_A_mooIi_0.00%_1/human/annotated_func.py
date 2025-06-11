#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of two lines. The first line contains a single integer n (2 <= n <= 100). The second line contains n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^9).
    for _ in range(int(input())):
        n = int(input())
        
        ar = map(str, sorted(list(map(int, input().split()))))
        
        print(' '.join(ar))
        
    #State: n is an integer equal to the input value, ar is a map object containing the sorted integers from the input as strings, stdin is empty, the sorted integers from the input as strings are printed, _ is equal to the number of test cases, and the sorted integers from the input as strings joined by a space are printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of a single integer n followed by n integers. It sorts the integers in ascending order, converts them to strings, and prints them joined by a space. The function repeats this process for each test case, emptying the standard input in the process.

