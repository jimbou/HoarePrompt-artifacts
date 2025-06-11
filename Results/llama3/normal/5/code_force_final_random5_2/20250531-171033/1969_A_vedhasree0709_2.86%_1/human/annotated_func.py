#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 5000) followed by t test cases. Each test case consists of an integer n (2 <= n <= 50) followed by n distinct integers p_1, p_2, ..., p_n (1 <= p_i <= n; p_i != i).
    for _ in range(int(input())):
        n = int(input())
        
        l = list(map(int, input().split()))
        
        i = 0
        
        j = 0
        
        while i <= n - 1:
            if l[i] == i + 2 and l[i + 1] == i + 1:
                print(2)
                j = 1
                break
            i += 1
        
        if j == 0:
            print(3)
        
    #State: i is n, j is either 0 or 1, n is an integer between 2 and 50 inclusive, l is a list of n distinct integers between 1 and n inclusive, t is 0. If there exists an index k such that l[k] equals k + 2 and l[k + 1] equals k + 1, then the number 2 is printed and j is 1. Otherwise, if j is 0, the number 3 is printed and j remains 0. If j is 1, no additional changes are made.

#Overall this is what the function does:The function reads a series of test cases from standard input, where each test case consists of an integer n followed by n distinct integers. It then checks each test case for a specific condition: if there exists a pair of adjacent integers where the first integer is 2 more than its index and the second integer is 1 more than its index, it prints 2. If no such pair is found, it prints 3. The function processes all test cases and prints the corresponding results.

