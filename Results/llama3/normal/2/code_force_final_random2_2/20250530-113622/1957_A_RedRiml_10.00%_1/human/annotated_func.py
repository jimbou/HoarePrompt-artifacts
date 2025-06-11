#State of the program right berfore the function call: stdin contains t test cases. Each test case contains two lines. The first line contains an integer n (1 <= n <= 100). The second line contains n integers a_1, a_2, ..., a_n (1 <= a_i <= 100).
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
                shapes += 1
        
        print(shapes)
        
    #State: w is 0, stdin is empty, ln is an integer between 1 and 100, palka is an empty list, pl is an empty list, d is an empty dictionary, j does not exist, and shapes is 0.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer n followed by n integers. It then counts the number of distinct integers that appear at least three times in each test case and prints this count. The function processes all test cases and leaves the input stream empty.

