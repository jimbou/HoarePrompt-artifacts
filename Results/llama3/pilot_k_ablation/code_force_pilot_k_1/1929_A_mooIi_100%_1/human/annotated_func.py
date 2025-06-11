#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of two lines. The first line contains a single integer n (2 <= n <= 100). The second line contains n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^9).
    for _ in range(int(input())):
        n = int(input())
        
        ar = list(sorted(list(map(int, input().split()))))
        
        print(sum([(ar[i] - ar[i - 1]) for i in range(1, n)]))
        
    #State: stdin is empty, _ is the number of test cases, n is not defined, ar is not defined

#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of a single integer n followed by n integers. It then calculates and prints the sum of the differences between consecutive integers in each test case, sorted in ascending order. After processing all test cases, the function leaves the standard input empty.

