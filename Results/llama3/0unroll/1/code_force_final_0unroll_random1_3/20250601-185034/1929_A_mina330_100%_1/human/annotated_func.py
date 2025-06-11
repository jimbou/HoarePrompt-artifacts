#State of the program right berfore the function call: stdin contains an integer t (1 ≤ t ≤ 500) followed by t test cases. Each test case consists of an integer n (2 ≤ n ≤ 100) followed by n integers a_1, a_2, …, a_n (1 ≤ a_i ≤ 10^9).
    ntest = int(input())
    for itest in range(0, ntest, 1):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        a.sort()
        
        print(a[len(a) - 1] - a[0])
        
    #State: The loop has executed `ntest` times, and for each test case, it has printed the difference between the largest and smallest numbers in the input list `a`. The value of `ntest` remains unchanged, and the input buffer is empty.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer n followed by n integers. For each test case, it calculates and prints the difference between the largest and smallest numbers in the input list. The function processes multiple test cases as specified by the initial input integer t, and it does not modify the input values or store any results beyond printing the differences for each test case.

