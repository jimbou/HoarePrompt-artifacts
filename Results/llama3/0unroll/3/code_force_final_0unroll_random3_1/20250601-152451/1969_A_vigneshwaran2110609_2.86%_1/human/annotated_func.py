#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 5000) followed by t test cases. Each test case consists of an integer n (2 <= n <= 50) followed by n distinct integers p_1, p_2, ..., p_n (1 <= p_i <= n; p_i != i).
    n = int(input())
    for i in range(n):
        x = int(input())
        
        l = list(map(int, input().strip().split()))
        
        for i in range(0, x):
            if l[l[i] - 1] == l[i] - 1:
                flag = True
                print(2)
                break
        else:
            print(3)
        
    #State: The loop will print either 2 or 3 for each test case. If a test case contains a pair of integers (p_i, p_j) such that p_i = p_j, it will print 2. Otherwise, it will print 3. The value of n remains unchanged.

#Overall this is what the function does:This function reads input from stdin, processes test cases, and prints the result for each case. It accepts no parameters and returns no value. The function iterates over the test cases, and for each case, it checks if there exists a pair of integers (p_i, p_j) such that p_i = p_j. If such a pair is found, it prints 2; otherwise, it prints 3. The function does not modify the input values and does not retain any state after execution.

