#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 3 * 10^4) followed by t test cases. Each test case consists of three lines: the first line contains two integers n and k (1 <= n <= 3 * 10^5, 1 <= k <= 2 * 10^9), the second line contains n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^9), and the third line contains n integers x_1, x_2, ..., x_n (-n <= x_1 < x_2 < ... < x_n <= n, x_i != 0). The sum of n over all test cases does not exceed 3 * 10^5.
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
        
    #State: The output state will be a series of 'YES' or 'NO' printed to the console, one for each test case, indicating whether the player can survive the monsters or not. The value of `t` will be unchanged, and the input from stdin will be consumed. The variables `n`, `k`, `a`, `x`, `monsters`, `bullets_used`, and `can_survive` will be reinitialized for each test case and will not retain any value after the loop finishes.

#Overall this is what the function does:This function reads input from stdin, processes multiple test cases, and prints 'YES' or 'NO' for each case, indicating whether a player can survive a series of monsters based on their health, distance, and the player's available bullets. The function does not modify the input or retain any values after execution.

