#State of the program right berfore the function call: stdin contains t test cases. Each test case contains two lines. The first line contains a single integer n (1 <= n <= 100). The second line contains n integers a_1, a_2, ..., a_n (1 <= a_i <= 100).
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
        
    #State: `w` is 0, `stdin` is empty, `ln` is an integer, `palka` is a list of integers, `pl` contains all unique integers in the list `palka`, `d` contains the key `x` with a value that is the frequency of `x` in the list `palka`, `shapes` is the sum of the integer divisions of the frequencies of all unique integers in `palka` by 3, and the sum of the integer divisions of the frequencies of all unique integers in `palka` by 3 which is equal to `shapes` is being printed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of a single integer n followed by n integers. It then counts the frequency of each unique integer in the list, calculates the sum of the integer divisions of these frequencies by 3, and prints this sum for each test case. The function continues this process until all test cases have been read from standard input, at which point the input is exhausted.

