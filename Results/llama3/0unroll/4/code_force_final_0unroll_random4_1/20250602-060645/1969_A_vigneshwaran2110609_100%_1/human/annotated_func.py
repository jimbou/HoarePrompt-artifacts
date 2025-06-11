#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 5000) followed by t test cases. Each test case consists of two lines: the first line contains an integer n (2 <= n <= 50), and the second line contains n distinct integers p_i (1 <= p_i <= n; p_i != i).
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
        
    #State: The output state will contain t lines, each containing either 2 or 3. For each test case, if there exists an index i such that the element at index l[i] - 1 is equal to i + 1, the output will be 2. Otherwise, the output will be 3. The value of n will remain unchanged, as it is not modified within the loop.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer n followed by a list of n distinct integers. It then checks for each test case if there exists an index i such that the element at index l[i] - 1 is equal to i + 1. If such an index exists, it prints 2; otherwise, it prints 3. The function repeats this process for all test cases and does not modify the input values.

