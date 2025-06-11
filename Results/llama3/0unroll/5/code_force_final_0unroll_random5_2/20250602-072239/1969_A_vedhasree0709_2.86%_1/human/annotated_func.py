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
        
    #State: The output state will be a list of integers, where each integer is either 2 or 3. The length of the list will be equal to the value of t in the initial state. For each test case, if there exists a pair of adjacent elements in the list l such that the first element is equal to the index of the second element plus 2, and the second element is equal to the index of the first element plus 1, then the output will be 2. Otherwise, the output will be 3.

#Overall this is what the function does:The function reads a series of test cases from standard input, where each test case consists of an integer n followed by n distinct integers. It then checks each test case for a specific condition: if there exists a pair of adjacent elements in the list such that the first element is equal to the index of the second element plus 2, and the second element is equal to the index of the first element plus 1, it prints 2. If no such pair is found, it prints 3. The function repeats this process for each test case and produces a list of output integers, either 2 or 3, corresponding to each test case.

