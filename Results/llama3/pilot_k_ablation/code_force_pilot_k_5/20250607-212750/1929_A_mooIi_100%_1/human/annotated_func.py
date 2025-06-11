#State of the program right berfore the function call: stdin contains an integer t (1 ≤ t ≤ 500) followed by t test cases. Each test case consists of an integer n (2 ≤ n ≤ 100) followed by n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^9).
    for _ in range(int(input())):
        n = int(input())
        
        ar = list(sorted(list(map(int, input().split()))))
        
        print(sum([(ar[i] - ar[i - 1]) for i in range(1, n)]))
        
    #State: n is an integer between 2 and 100 inclusive, ar is a sorted list of n integers between 1 and 10^9 inclusive, stdin contains 0 test cases, _ is t-1, and the sum of the differences between consecutive elements in the list ar is printed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer n followed by n integers. It sorts the integers in ascending order, calculates the sum of the differences between consecutive integers, and prints this sum for each test case. The function processes all test cases and then terminates, leaving the standard input empty.

