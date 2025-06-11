#State of the program right berfore the function call: stdin contains an integer t (1 ≤ t ≤ 500) followed by t test cases. Each test case consists of an integer n (2 ≤ n ≤ 100) followed by n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^9).
    for _ in range(int(input())):
        n = int(input())
        
        ar = map(str, sorted(list(map(int, input().split()))))
        
        print(' '.join(ar))
        
    #State: stdin contains no input, and the standard output contains t lines, each containing n sorted integers separated by spaces.

#Overall this is what the function does:Reads a series of test cases from standard input, where each test case consists of an integer n followed by n integers, sorts the integers in ascending order, and prints the sorted integers to standard output, one test case per line.

