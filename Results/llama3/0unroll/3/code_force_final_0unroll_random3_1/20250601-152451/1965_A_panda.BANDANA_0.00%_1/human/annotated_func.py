#State of the program right berfore the function call: stdin contains t test cases. Each test case contains two inputs: first an integer n (1 <= n <= 2*10^5) and then n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^9).
    t = int(input())
    for i in range(t):
        n = int(input())
        
        l = list(map(int, input().split()))
        
        e = set(l)
        
        m = len(l)
        
        if 1 in l:
            print('Bob')
        else:
            print('Alice')
        
    #State: The loop will execute t times, each time reading a test case from stdin. For each test case, it will print 'Bob' if the number 1 is present in the input list, and 'Alice' otherwise. The output will be a sequence of t lines, each containing either 'Bob' or 'Alice'. The value of t will be decremented by 1 after each iteration, and the input list l will be overwritten with the next test case. The set e and the variable m will also be updated accordingly.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer n followed by n integers. It then checks if the number 1 is present in the input list. If 1 is found, it prints 'Bob'; otherwise, it prints 'Alice'. This process is repeated for each test case, resulting in a sequence of 'Bob' or 'Alice' outputs, one for each test case.

