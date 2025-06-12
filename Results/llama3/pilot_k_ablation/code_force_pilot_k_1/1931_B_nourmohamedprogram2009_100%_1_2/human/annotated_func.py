#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of two lines. The first line contains a single integer n (1 <= n <= 2 * 10^5). The second line contains n integers a_1, a_2, ..., a_n (0 <= a_i <= 10^9) such that the sum of a_i is divisible by n. The sum of n over all test cases does not exceed 2 * 10^5.
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
        
    #State: `t` is 0, `_` is `t`, `n` is an integer, `a` is a list of integers, `total_water` is the sum of the integers in `a`, `target` is the integer division of `total_water` by `n`, `current_balance` is the sum of the differences between each element of `a` and `target`, `possible` is a boolean indicating whether `current_balance` was never less than 0 during the loop. The output will contain 'YES' or 'NO' for each test case, depending on the value of `possible`.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of a list of integers. It determines whether it's possible to redistribute the integers such that each integer is equal to the average of the list, by checking if the cumulative sum of differences between each integer and the average ever becomes negative. For each test case, it prints 'YES' if redistribution is possible and 'NO' otherwise.

