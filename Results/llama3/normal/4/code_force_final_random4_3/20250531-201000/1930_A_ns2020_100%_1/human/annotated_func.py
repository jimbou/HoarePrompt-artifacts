#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line contains a single integer n (1 ≤ n ≤ 50). The second line contains 2n integers a_1,a_2,…,a_{2n} (1 ≤ a_i ≤ 10^7).
    t = int(input())
    while t:
        n = int(input())
        
        A = list(map(int, input().split()))
        
        A.sort()
        
        print(sum(A[::2]))
        
        t = t - 1
        
    #State: `t` is 0, `n` is an integer equal to the input value, `A` is a sorted list of 2 integers, and the sum of every other element in the list `A` starting from the first element is being printed.

#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of a single integer n followed by 2n integers. It sorts the 2n integers in ascending order and prints the sum of every other integer starting from the first one. The function repeats this process for each test case until all cases have been processed.

