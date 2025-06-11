#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case contains an integer n (1 <= n <= 2 * 10^5) followed by n integers a_1, a_2, ..., a_n (0 <= a_i <= 10^9) such that the sum of a_i is divisible by n.
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
        
    #State: t is an integer and is at least 0, stdin contains 0 test cases, n is an integer between 1 and 2 * 10^5 inclusive, a is a list of n integers between 0 and 10^9 inclusive, total_water is the sum of the integers in a, target is the sum of the integers in a divided by n, i is n, _ is 0, current_balance is the sum of the integers in a minus n times the target. If current_balance is not less than 0 at any point, then 'YES' is printed. Otherwise, 'NO' is printed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer n followed by n integers. It calculates the average of these integers and checks if it's possible to redistribute the integers such that each integer is equal to the average. If this is possible for all test cases, it prints 'YES' for each test case; otherwise, it prints 'NO'.

