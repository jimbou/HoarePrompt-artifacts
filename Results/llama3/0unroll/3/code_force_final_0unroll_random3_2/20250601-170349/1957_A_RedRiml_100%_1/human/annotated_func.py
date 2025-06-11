#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 100) followed by t test cases. Each test case consists of an integer n (1 <= n <= 100) followed by n integers a_1, a_2, ..., a_n (1 <= a_i <= 100).
    w = int(input())
    for _ in range(w):
        ln = int(input())
        
        palka = list(map(int, input().split()))
        
        pl = []
        
        d = {}
        
        for i in palka:
            if d.get(i) == None:
                d[i] = 1
            else:
                d[i] += 1
            if i not in pl:
                pl.append(i)
        
        shapes = 0
        
        for j in pl:
            if d[j] >= 3:
                shapes += d[j] // 3
        
        print(shapes)
        
    #State: The output state will be the total number of shapes that can be formed from the given test cases, where each shape is formed by 3 identical integers. The output will be a series of integers, each representing the total number of shapes that can be formed from the corresponding test case. The state of the variable 'w' will be unchanged, as it is not affected by the loop head and body.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of a list of integers. It then calculates and prints the total number of shapes that can be formed from each test case, where a shape is defined as a set of three identical integers. The function does not modify the input data and does not have any side effects beyond printing the results.

