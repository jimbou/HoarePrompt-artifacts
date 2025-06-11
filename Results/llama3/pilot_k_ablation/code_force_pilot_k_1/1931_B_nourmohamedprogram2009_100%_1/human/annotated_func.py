#State of the program right berfore the function call: stdin contains multiple inputs: first an integer t (1 <= t <= 10^4), then for each test case, first an integer n (1 <= n <= 2 * 10^5) and then n integers a_1, a_2, ..., a_n (0 <= a_i <= 10^9) such that the sum of a_i is divisible by n.
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        total_water = sum(a)
        
        target = total_water // n
        
        current_balance = 0
        
        possible = True
        
        for i in range(n):
            current_balance += a[i] - target
            if current_balance < 0:
                possible = False
                break
        
        if possible:
            print('YES')
        else:
            print('NO')
        
    #State: `t` is an integer between 0 and 10^4, `_` is `t`, `n` is the last integer input, `a` is the last list of integers input, `total_water` is the sum of the last list of integers input, `target` is the integer division of `total_water` by `n`, `current_balance` is the sum of the differences between each integer in the last list of integers input and the target, `possible` is True if the last list of integers can be balanced, False otherwise.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer n and a list of n integers. It calculates the total sum of the integers and checks if it's possible to balance the list by redistributing the integers to make them all equal to the average value. If balancing is possible, it prints 'YES', otherwise it prints 'NO'. The function repeats this process for all test cases.

