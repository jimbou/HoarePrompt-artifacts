#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 100) followed by t test cases. Each test case contains an integer n (1 <= n <= 100) followed by n integers a_1, a_2, ..., a_n (1 <= a_i <= 100).
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
        
    #State: The loop will execute `w` times, where `w` is an integer between 1 and 100 inclusive. In each iteration, it will read a line from stdin containing an integer `n` (1 <= `n` <= 100) followed by `n` integers `a_1`, `a_2`, ..., `a_n` (1 <= `a_i` <= 100). It will then count the number of unique integers in the input that appear at least three times and print this count. The output will be a sequence of `w` integers, each representing the count of such unique integers in the corresponding test case.

#Overall this is what the function does:This function reads a sequence of test cases from standard input, where each test case consists of an integer n followed by n integers. It then counts the number of unique integers in each test case that appear at least three times and prints this count for each test case. The function processes multiple test cases, with the number of test cases specified by the first integer read from standard input.

