#State of the program right berfore the function call: stdin contains an integer t (1 ≤ t ≤ 500) followed by t test cases. Each test case consists of an integer n (2 ≤ n ≤ 100) followed by n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^9).
    for _ in range(int(input())):
        n = int(input())
        
        ar = map(str, sorted(list(map(int, input().split()))))
        
        print(' '.join(ar))
        
    #State: n is an integer equal to the last input integer, ar is a list of strings representing the sorted input integers, stdin contains 0 test cases, _ is t-1, and the sorted input integers are printed as a string separated by spaces, and this is printed: t-1 strings of sorted input integers separated by spaces.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer n followed by n integers. It sorts each set of integers in ascending order and prints them as a string separated by spaces. The function continues this process until all test cases have been read from standard input, at which point it terminates.

