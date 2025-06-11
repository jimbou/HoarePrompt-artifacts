#State of the program right berfore the function call: stdin contains two inputs: first an integer (the number of test cases) and then a sequence of integers (the values of X for each test case). Each value of X is a positive integer such that 2 <= X <= 10^18.
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
        
    #State: x is 1, t is a positive integer, max is either 100000000 minus the number of times the loop executed if x was originally even, or 100000000 minus the number of times the loop executed plus 1 if x was originally odd, min is either -100000000 plus the number of times the loop executed if x was originally odd, or -100000000 plus the number of times the loop executed minus 1 if x was originally even, ans is a list containing the values of min and max in the order they were appended, and the number of times the loop executed which is t is being printed, and the list ans containing the values of min and max is being printed.

#Overall this is what the function does:This function reads a sequence of positive integers from standard input, where each integer represents a value X. For each X, it performs a series of operations, appending either a decreasing sequence of positive integers (starting from 100,000,000) or an increasing sequence of negative integers (starting from -100,000,000) to a list, until X becomes 1. The function then prints the number of operations performed and the list of appended integers in reverse order. The function repeats this process for each input value X.

