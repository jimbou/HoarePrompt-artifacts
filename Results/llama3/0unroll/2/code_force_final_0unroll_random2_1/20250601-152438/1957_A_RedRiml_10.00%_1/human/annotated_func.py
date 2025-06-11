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
                shapes += 1
        
        print(shapes)
        
    #State: The number of integers that appear at least three times in each test case is printed to the console. The input state remains unchanged, with 'w' still being an integer between 1 and 100, and stdin containing 'w' test cases. Each test case still consists of an integer 'n' (1 <= n <= 100) followed by 'n' integers 'a_1', 'a_2', ..., 'a_n' (1 <= a_i <= 100).

#Overall this is what the function does:The function reads a series of test cases from standard input, where each test case consists of an integer 'n' followed by 'n' integers. It then counts the number of integers that appear at least three times in each test case and prints this count to the console. The function does not modify the input state, and the input remains unchanged after execution.

