#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 3 * 10^4) followed by t test cases. Each test case consists of three lines: the first line contains two integers n and k (1 <= n <= 3 * 10^5; 1 <= k <= 2 * 10^9), the second line contains n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^9), and the third line contains n integers x_1, x_2, ..., x_n (-n <= x_1 < x_2 < ... < x_n <= n; x_i != 0). The sum of n over all test cases does not exceed 3 * 10^5.
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
        
    #State: t is an integer between 0 and 3 * 10^4 (inclusive), stdin contains 0 test cases, _ is t, n is an integer, k is an integer, a is a list of integers, x is a list of integers, monsters is an empty list, bullets_used is the sum of the health values of all monsters, can_survive is False if total_bullets_needed is more than distance * k for any monster, otherwise can_survive is True, and 'YES' is printed if can_survive is True, otherwise 'NO' is printed.

#Overall this is what the function does:Determines whether a player can survive a series of monster attacks based on the number of bullets used and the distance to each monster, and prints 'YES' if the player can survive and 'NO' otherwise.

