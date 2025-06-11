#State of the program right berfore the function call: stdin contains an integer t (1 ≤ t ≤ 500) followed by t test cases. Each test case consists of an integer n (2 ≤ n ≤ 100) followed by n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^9).
    for _ in range(int(input())):
        n = int(input())
        
        ar = map(str, sorted(list(map(int, input().split()))))
        
        print(' '.join(ar))
        
    #State: The output state is a series of t lines, each containing n sorted integers separated by spaces, where t is the initial integer input and n is the number of integers in each test case. The integers in each line are sorted in ascending order.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer n followed by n integers. It sorts the integers in ascending order and prints them to standard output, one test case per line. The function processes multiple test cases, with the number of test cases specified by an initial integer input.

