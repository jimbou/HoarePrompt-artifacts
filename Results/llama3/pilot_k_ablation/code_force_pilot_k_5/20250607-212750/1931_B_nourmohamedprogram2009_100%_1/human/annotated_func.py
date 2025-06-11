#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case consists of an integer n (1 <= n <= 2 * 10^5) followed by n integers a_1, a_2, ..., a_n (0 <= a_i <= 10^9) such that the sum of a_i is divisible by n.
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
        
    #State: t is an integer between 0 and 10^4 inclusive, n is an integer greater than or equal to 0, i is equal to n, a is a list of integers, total_water is the sum of all elements in a, target is the integer division of total_water by n, current_balance is the sum of all elements in a minus n times the target, possible is True if current_balance is greater than or equal to 0, otherwise possible is False, and _ is equal to t. stdin is empty.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer n followed by n integers. It determines whether it is possible to distribute the sum of the integers evenly among n containers, and prints 'YES' if possible and 'NO' otherwise. The function processes all test cases and then terminates, leaving the standard input empty.

