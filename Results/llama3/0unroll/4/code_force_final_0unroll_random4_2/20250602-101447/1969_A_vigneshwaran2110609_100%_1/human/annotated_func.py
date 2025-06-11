#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 5000) followed by t test cases. Each test case consists of two lines: the first line contains an integer n (2 <= n <= 50), and the second line contains n distinct integers p_1, p_2, ..., p_n (1 <= p_i <= n; p_i != i).
    n = int(input())
    for i in range(n):
        x = int(input())
        
        l = list(map(int, input().strip().split()))
        
        for i in range(0, x):
            if l[l[i] - 1] == i + 1:
                flag = True
                print(2)
                break
        else:
            print(3)
        
    #State: The loop will print either 2 or 3 for each test case. If a test case contains a pair of integers (p_i, p_j) such that p_i = j and p_j = i, it will print 2. Otherwise, it will print 3. The value of n will remain unchanged.

#Overall this is what the function does:The function reads a series of test cases from standard input, where each test case consists of an integer n followed by n distinct integers. It then checks each test case for a specific condition, printing 2 if the condition is met (i.e., a pair of integers (p_i, p_j) exists such that p_i = j and p_j = i) and 3 otherwise. The function does not modify the input values and only prints the results for each test case.

