#State of the program right berfore the function call: stdin contains an integer t (1 ≤ t ≤ 500) followed by t test cases. Each test case contains an integer n (2 ≤ n ≤ 100) followed by n integers a_1, a_2, …, a_n (1 ≤ a_i ≤ 10^9).
    t = int(input().strip())
    for i in range(t):
        n = int(input().strip())
        
        ls = input().split()
        
        last = int(ls.pop())
        
        other = int(sorted(ls).pop())
        
        print(last + other)
        
    #State: The output will be the sum of the last element and the second largest element of each test case, printed on a new line for each test case. The value of `t` will be unchanged, and the contents of stdin will be consumed.

#Overall this is what the function does:The function reads a series of test cases from standard input, where each test case contains a list of integers. For each test case, it identifies the last element and the second-largest element, and prints their sum to standard output. The function consumes the contents of standard input and leaves the value of `t` unchanged.

