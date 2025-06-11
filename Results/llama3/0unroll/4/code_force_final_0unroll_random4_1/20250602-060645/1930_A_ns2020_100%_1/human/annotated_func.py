#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 5000) followed by t test cases. Each test case contains an integer n (1 <= n <= 50) followed by 2n integers a_1,a_2,...,a_{2n} (1 <= a_i <= 10^7).
    t = int(input())
    while t:
        n = int(input())
        
        A = list(map(int, input().split()))
        
        A.sort()
        
        print(sum(A[::2]))
        
        t = t - 1
        
    #State: t is 0, and the sum of every other integer from each test case, starting from the smallest integer, is printed to the console.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case contains an even number of integers. It sorts the integers in ascending order, then prints the sum of every other integer, starting from the smallest. The function processes multiple test cases, with the number of test cases specified at the beginning of the input.

