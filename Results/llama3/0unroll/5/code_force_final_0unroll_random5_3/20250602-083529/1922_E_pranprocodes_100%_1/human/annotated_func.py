#State of the program right berfore the function call: stdin contains two inputs: first an integer (the number of test cases) and then a list of integers (the values of X). Each X is a positive integer such that 2 <= X <= 10^18.
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
        
    #State: The output state will contain the number of test cases (which remains unchanged) followed by the modified list of integers. Each integer in the list will be replaced by the number of operations (t) required to reduce it to 1, followed by the sequence of numbers (ans) obtained by reversing the sequence of operations performed on the original number. The sequence of numbers will start with the maximum or minimum value (depending on whether the original number was even or odd) and will decrease or increase by 1 in each step, respectively.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of a positive integer X. It then performs a sequence of operations on each X, repeatedly dividing by 2 if X is even or subtracting 1 if X is odd, until X becomes 1. The function keeps track of the number of operations (t) and the sequence of numbers obtained by reversing the sequence of operations. Finally, it prints the number of operations (t) and the reversed sequence of numbers for each test case.

