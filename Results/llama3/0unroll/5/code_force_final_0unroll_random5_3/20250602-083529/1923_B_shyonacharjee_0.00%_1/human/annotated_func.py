#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 3 * 10^4) followed by t test cases. Each test case consists of three lines: the first line contains two integers n and k (1 <= n <= 3 * 10^5, 1 <= k <= 2 * 10^9), the second line contains n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^9), and the third line contains n integers x_1, x_2, ..., x_n (-n <= x_1 < x_2 < ... < x_n <= n, x_i != 0). The sum of n over all test cases does not exceed 3 * 10^5.
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
        
    #State: Output State: The output state after the loop executes all the iterations is a series of 'YES' or 'NO' strings, each representing whether the test case was successful or not. The number of strings is equal to the initial value of 't'. The values of 'n', 'k', 'healths', 'positions', and 'monsters' are unchanged, as they are not affected by the loop head and body. The 'total_bullets_used' and 'success' variables are reset to 0 and True, respectively, at the beginning of each iteration, so their final values are not meaningful.

#Overall this is what the function does:This function reads input from stdin, processes multiple test cases, and outputs a series of 'YES' or 'NO' strings indicating whether each test case was successful or not. It takes no parameters and returns no values, only printing the results to the console. The function's purpose is to determine whether a set of monsters can be defeated with a limited number of bullets, considering their positions and health points. It performs the following actions: reads input data, sorts monsters by their distance, calculates the total bullets used, and checks if the total bullets used exceeds the time available. Based on this calculation, it outputs 'YES' if the test case is successful and 'NO' otherwise.

