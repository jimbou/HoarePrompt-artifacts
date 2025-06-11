#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three lines: the first line contains two integers n and k (1 <= n <= 3 * 10^5, 1 <= k <= 2 * 10^9), the second line contains n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^9), and the third line contains n integers x_1, x_2, ..., x_n (-n <= x_1 < x_2 < x_3 < ... < x_n <= n; x_i != 0). The sum of n over all test cases does not exceed 3 * 10^5.
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        x = list(map(int, input().split()))
        
        monsters = sorted(zip(x, a), key=lambda p: abs(p[0]))
        
        bullets_used = 0
        
        can_survive = True
        
        for pos, health in monsters:
            distance = abs(pos)
            total_bullets_needed = bullets_used + health
            if total_bullets_needed > distance * k:
                can_survive = False
                break
            bullets_used += health
        
        print('YES' if can_survive else 'NO')
        
    #State: t is a positive integer and must be 0, _ is equal to the initial value of t, n is an integer between 1 and 3 * 10^5, k is an integer between 1 and 2 * 10^9, a is a list of n integers between 1 and 10^9, x is a list of n integers between -n and n, monsters is an empty list, bullets_used is the sum of the health of all monsters, can_survive is False if the total bullets needed to kill any monster is greater than the product of the distance to that monster and k, otherwise can_survive is True, stdin contains no test cases, and 'YES' is printed if can_survive is True, otherwise 'NO' is printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of three lines: two integers n and k, a list of n integers a, and a list of n integers x. It then determines whether it is possible to survive a series of monster attacks based on the given parameters. The function prints 'YES' if survival is possible and 'NO' otherwise.

