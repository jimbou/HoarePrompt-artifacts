#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line contains a single integer n (1 ≤ n ≤ 50). The second line contains 2n integers a_1,a_2,…,a_{2n} (1 ≤ a_i ≤ 10^7).
    t = int(input())
    while t:
        n = int(input())
        
        A = list(map(int, input().split()))
        
        print(sum(A[::2]))
        
        t = t - 1
        
    #State: t is 0, n is an integer, A is a list of integers, stdin contains no test cases, the sum of every other element in the list A starting from the first element for all test cases has been printed

#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of an integer n followed by 2n integers. It then calculates and prints the sum of every other element in the list of integers, starting from the first element, for each test case. The function continues this process until all test cases have been processed, at which point it terminates, leaving the input stream empty.

