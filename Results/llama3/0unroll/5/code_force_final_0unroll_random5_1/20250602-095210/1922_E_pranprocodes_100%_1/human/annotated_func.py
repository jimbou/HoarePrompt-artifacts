#State of the program right berfore the function call: stdin contains two inputs: first an integer (the number of test cases) and then a sequence of integers (the values of X). Each X is a positive integer such that 2 <= X <= 10^18.
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
        
    #State: The output state will contain the number of test cases (an integer) followed by a sequence of integers representing the number of operations (t) and the sequence of numbers (ans) for each test case. The sequence of numbers (ans) will be in reverse order, with the first number being the maximum or minimum value (depending on whether the input X is even or odd) and the subsequent numbers being the result of the operations performed on X. The state of the other variables (stdin, max, min) remains unchanged.

#Overall this is what the function does:This function reads a sequence of positive integers from standard input, applies a series of operations to each integer (alternating between dividing by 2 and subtracting 1), and prints the number of operations performed and the resulting sequence of numbers in reverse order. The function processes multiple test cases, with the number of test cases specified in the first input.

