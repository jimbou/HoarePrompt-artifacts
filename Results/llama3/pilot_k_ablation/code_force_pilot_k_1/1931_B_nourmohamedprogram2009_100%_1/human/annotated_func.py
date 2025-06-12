#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case consists of an integer n (1 <= n <= 2 * 10^5) followed by n integers a_1, a_2, ..., a_n (0 <= a_i <= 10^9). The sum of a_i is divisible by n.
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
        
    #State: t is 0, stdin contains 0 test cases, n is not defined, a is not defined, total_water is not defined, target is not defined, current_balance is not defined, possible is not defined, _ is t.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer n followed by n integers. It calculates the average of these integers and checks if it's possible to balance the water among n containers by redistributing the water without exceeding the capacity of any container. If balancing is possible, it prints 'YES'; otherwise, it prints 'NO'. The function processes all test cases and then terminates, leaving the input stream empty.

