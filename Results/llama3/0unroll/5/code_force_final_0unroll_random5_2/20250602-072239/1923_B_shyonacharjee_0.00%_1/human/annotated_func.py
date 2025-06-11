#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 3 * 10^4) followed by t test cases. Each test case consists of three lines: the first line contains two integers n and k (1 <= n <= 3 * 10^5, 1 <= k <= 2 * 10^9), the second line contains n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^9), and the third line contains n integers x_1, x_2, ..., x_n (-n <= x_1 < x_2 < x_3 < ... < x_n <= n, x_i != 0). The sum of n over all test cases does not exceed 3 * 10^5.
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
        
    #State: The output state will be a series of 'YES' or 'NO' printed to the console, each corresponding to whether the test case was successful or not. The number of 'YES' or 'NO' printed will be equal to the number of test cases t. The values of t, n, k, healths, positions, monsters, total_bullets_used, and success will be updated after each iteration of the loop, but their final values will not be printed. The stdin will be empty after the loop finishes executing.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of a number of monsters with their health and position. It then determines whether it is possible to kill all monsters with a limited number of bullets, based on their distance and health. The function prints 'YES' if it is possible to kill all monsters and 'NO' otherwise, for each test case.

