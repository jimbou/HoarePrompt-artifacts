#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three lines. The first line contains two integers n and k (1 <= n <= 3 * 10^5, 1 <= k <= 2 * 10^9). The second line contains n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^9). The third line contains n integers x_1, x_2, ..., x_n (-n <= x_1 < x_2 < ... < x_n <= n, x_i != 0). The sum of n over all test cases does not exceed 3 * 10^5.
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        
        healths = list(map(int, input().split()))
        
        positions = list(map(int, input().split()))
        
        monsters = sorted(zip(positions, healths), key=lambda x: abs(x[0]))
        
        total_bullets_used = 0
        
        success = True
        
        for i in range(n):
            position, health = monsters[i]
            distance = abs(position)
            time_available = distance
            bullets_needed = health
            if total_bullets_used + bullets_needed > time_available:
                success = False
                break
            total_bullets_used += bullets_needed
        
        print('YES' if success else 'NO')
        
    #State: t is 0, n is an integer, k is an integer, healths is a list of integers, positions is a list of integers, monsters is a sorted list of tuples containing integers, stdin is empty, i is n-1, position is the position of the last monster, health is the health of the last monster, distance is the absolute value of the position of the last monster, time_available is the absolute value of the position of the last monster, bullets_needed is the health of the last monster, total_bullets_used is the sum of the health of all monsters, success is True if total_bullets_used is less than or equal to the absolute value of the position of the last monster, otherwise False, and 'YES' or 'NO' is printed for each test case depending on whether success is True or False.

#Overall this is what the function does:This function determines whether it is possible to kill all monsters in a game scenario. It reads multiple test cases from standard input, where each test case consists of three lines: the number of monsters and a limit, the health of each monster, and the position of each monster. The function then simulates the game, sorting the monsters by their distance from the player and attempting to kill them in that order. It keeps track of the total bullets used and checks if it is possible to kill each monster with the available bullets. If it is possible to kill all monsters, it prints 'YES', otherwise it prints 'NO'. The function repeats this process for each test case.

