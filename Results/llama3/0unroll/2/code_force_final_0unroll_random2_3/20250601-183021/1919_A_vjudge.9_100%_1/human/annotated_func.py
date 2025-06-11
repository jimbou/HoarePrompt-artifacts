#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two space-separated integers a and b (1 <= a, b <= 10^9).
    t = int(input())
    for i in range(t):
        a, b = list(map(int, input().split(' ')))
        
        if abs(a - b) % 2 == 0:
            print('Bob')
        else:
            print('Alice')
        
    #State: Output State: The loop will print 'Bob' or 'Alice' for each test case, depending on whether the absolute difference between `a` and `b` is even or odd, respectively. The number of test cases `t` remains unchanged.

#Overall this is what the function does:Determines the winner ('Alice' or 'Bob') for each test case based on whether the absolute difference between two input integers is even or odd, and prints the result for each test case.

