#State of the program right berfore the function call: stdin contains two inputs: first an integer (the number of test cases) and then for each test case two space-separated integers (the number of applications with a 1x1 icon and the number of applications with a 2x2 icon, respectively). Both integers are non-negative and less than or equal to 99.
    n = int(input())
    for i in range(n):
        a, b = input().split()
        
        a = int(a)
        
        b = int(b)
        
        t = b
        
        if t % 2 == 0:
            t = t // 2
        else:
            t = t // 2 + 1
        
        t1 = t * 15 - b * 4
        
        if t1 >= a:
            t = t
        else:
            t2 = a - t1
            if t2 % 15 == 0:
                t = t + t2 // 15
            else:
                t = t + t2 // 15 + 1
        
        print(t)
        
    #State: The number of 2x2 icons required to cover the remaining area after using all the 1x1 icons, for each of the n applications, is printed on a new line.

#Overall this is what the function does:This function reads input from stdin, processes it, and prints output. It accepts no parameters and returns no value. It reads an integer (the number of test cases) and then for each test case, it reads two space-separated integers (the number of applications with a 1x1 icon and the number of applications with a 2x2 icon). It calculates the number of 2x2 icons required to cover the remaining area after using all the 1x1 icons for each application and prints the result on a new line.

