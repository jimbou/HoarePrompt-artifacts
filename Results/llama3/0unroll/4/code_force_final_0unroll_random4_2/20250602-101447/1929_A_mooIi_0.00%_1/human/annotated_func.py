#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line contains an integer n (2 <= n <= 100). The second line contains n space-separated integers a_i (1 <= a_i <= 10^9).
    for _ in range(int(input())):
        n = int(input())
        
        ar = map(str, sorted(list(map(int, input().split()))))
        
        print(' '.join(ar))
        
    #State: The output will be the sorted integers for each test case, in ascending order, separated by spaces.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer n followed by n space-separated integers. It sorts the integers in ascending order and prints them separated by spaces for each test case.

