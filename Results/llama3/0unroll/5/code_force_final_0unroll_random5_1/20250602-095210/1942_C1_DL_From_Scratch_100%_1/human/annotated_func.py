#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of two lines. The first line contains three integers: n, x, and y, where n is the number of sides of a polygon, x is the number of vertices Bessie has chosen, and y is the maximum number of other vertices that can be chosen (y = 0). The second line contains x distinct integers from 1 to n, representing the vertices Bessie has chosen.
    T = int(input())
    for _ in range(T):
        n, x, y = map(int, input().split())
        
        list0 = list(map(int, input().split()))
        
        list0 = sorted(list0)
        
        count = 0
        
        for i in range(x - 1):
            num = list0[i + 1] - list0[i] - 1
            if num == 1:
                count += 1
        
        num = list0[0] + n - list0[-1] - 1
        
        if num == 1:
            count += 1
        
        print(count + x - 2)
        
    #State: The output state will be the number of vertices that can be chosen by Bessie in each test case, which is the sum of the count of vertices that are one unit away from each other and the number of vertices Bessie has already chosen minus 2. The output will be in the format of a list of integers, where each integer represents the number of vertices that can be chosen in each test case.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of a polygon with a specified number of sides and vertices chosen by Bessie. It calculates and prints the total number of vertices that can be chosen by Bessie in each test case, considering the vertices that are one unit away from each other and the vertices Bessie has already chosen, minus 2. The output is a list of integers, each representing the number of vertices that can be chosen in each test case.

