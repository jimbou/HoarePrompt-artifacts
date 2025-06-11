#State of the program right berfore the function call: stdin contains two inputs: first an integer (the number of test cases) and then for each test case two space-separated integers (the number of applications with a 1x1 icon and the number of applications with a 2x2 icon, respectively). Both integers are non-negative and less than or equal to 99.
    ap = int(input())
    for k in range(ap):
        x, y = map(int, input().split())
        
        if x > 0 and y > 0:
            bxsfory = math.ceil(y / 2)
            x = x - bxsfory * 15 + y * 4
            bxsfory1 = 0 if x <= 0 else math.ceil(x / 15)
            print(bxsfory1 + bxsfory)
        elif x == 0 and y > 0:
            print(math.ceil(y / 2))
        elif x > 0 and y == 0:
            print(math.ceil(x / 15))
        else:
            print(0)
        
    #State: Output State: The loop will print the total number of boxes required for each test case, where the number of boxes is calculated based on the number of applications with 1x1 and 2x2 icons. The output will be a series of integers, one for each test case, representing the total number of boxes required.

#Overall this is what the function does:This function reads input from stdin, processes it, and prints the total number of boxes required for each test case. It accepts two inputs: the number of test cases and, for each test case, two space-separated integers representing the number of applications with 1x1 and 2x2 icons. The function calculates the total number of boxes required based on these inputs and prints the result for each test case.

