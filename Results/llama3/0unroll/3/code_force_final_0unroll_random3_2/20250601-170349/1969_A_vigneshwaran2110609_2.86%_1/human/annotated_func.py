#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 5000) followed by t test cases. Each test case consists of an integer n (2 <= n <= 50) followed by n distinct integers p_i (1 <= p_i <= n; p_i != i).
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
        
    #State: The output state will be a series of numbers, either 2 or 3, each on a new line, equal to the number of test cases (t-1). For each test case, if there exists an integer p_i such that p_i is equal to the (p_i-1)th integer in the list, the output will be 2. Otherwise, the output will be 3.

#Overall this is what the function does:The function reads a series of test cases from standard input, where each test case consists of an integer n followed by n distinct integers. For each test case, it checks if there exists an integer p_i such that p_i is equal to the (p_i-1)th integer in the list. If such an integer is found, it prints 2; otherwise, it prints 3. The function repeats this process for all test cases and outputs the results, one per line, without modifying the input data.

