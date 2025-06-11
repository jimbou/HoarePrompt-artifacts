#State of the program right berfore the function call: stdin contains two inputs: first an integer (the number of test cases) and then a sequence of integers (the test cases). Each test case is a positive integer (X) such that 2 <= X <= 10^18.
    for i in range(int(input())):
        x = int(input())
        
        max = 100000000
        
        min = -100000000
        
        ans = []
        
        t = 0
        
        while x != 1:
            if x % 2 == 0:
                ans.append(max)
                max -= 1
                x = x // 2
            else:
                ans.append(min)
                min += 1
                x -= 1
            t += 1
        
        ans.reverse()
        
        print(t)
        
        print(*ans)
        
    #State: Output State: The output state after the loop executes all the iterations is a sequence of integers, where each integer represents the number of operations (t) required to reduce the corresponding input integer (X) to 1, followed by the sequence of integers (ans) that represent the operations performed to reduce X to 1. The sequence of integers is in reverse order, with the last operation performed first. The output state is printed to the console, with each test case's output on a new line.

#Overall this is what the function does:This function reads a sequence of positive integers from standard input, where each integer represents a test case. For each test case, it performs a series of operations to reduce the integer to 1, either by dividing it by 2 if it's even or subtracting 1 if it's odd. The function then prints the number of operations required to reduce the integer to 1, followed by the sequence of operations performed in reverse order. The output is printed to the console, with each test case's output on a new line.

