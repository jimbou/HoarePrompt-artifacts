#State of the program right berfore the function call: stdin contains t test cases. Each test case contains two lines. The first line contains a single integer n (1 ≤ n ≤ 100). The second line contains n integers a_1, a_2, …, a_n (1 ≤ a_i ≤ 100).
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
        
    #State: Output State: The loop will have executed `w` times, where `w` is an integer between 1 and 100 inclusive. The input state will have been consumed, and the output will be `w` lines, each containing a single integer representing the number of shapes that can be formed from the given integers. The value of `w` will remain unchanged.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of a line with an integer n, followed by a line with n integers. It then processes each test case by counting the occurrences of each integer, identifies the unique integers, and calculates the number of shapes that can be formed by grouping the integers into sets of three. The function prints the number of shapes for each test case, consuming the input state and producing an output state with the calculated shape counts.

