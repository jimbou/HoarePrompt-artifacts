#State of the program right berfore the function call: stdin contains one integer t (1 <= t <= 3 * 10^4) followed by t test cases. Each test case consists of three lines: the first line contains two integers n and k (1 <= n <= 3 * 10^5; 1 <= k <= 2 * 10^9), the second line contains n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^9), and the third line contains n integers x_1, x_2, ..., x_n (-n <= x_1 < x_2 < x_3 < ... < x_n <= n; x_i != 0). The sum of n over all test cases does not exceed 3 * 10^5.
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
        
    #State: t is an integer between 1 and 3 * 10^4, _ is t-1, n is an integer equal to the first input integer, k is an integer equal to the second input integer, healths is a list of integers from the second input, positions is a list of integers from the third input, monsters is a sorted list of tuples containing integers from the second and third inputs, i is n-1, position is the position of the last monster, health is the health of the last monster, distance is the absolute value of the position of the last monster, time_available is the absolute value of the position of the last monster, bullets_needed is the health of the last monster, total_bullets_used is the sum of the health of all monsters, and success is False if the sum of the total bullets used and the bullets needed is greater than the time available, otherwise success remains True, and either 'YES' or 'NO' is printed depending on whether success is True or False, where 'YES' means the sum of the total bullets used and the bullets needed is less than or equal to the time available, and 'NO' means the sum of the total bullets used and the bullets needed is greater than the time available.

#Overall this is what the function does:This function determines whether it is possible to defeat a series of monsters with a limited number of bullets. It takes as input the number of test cases, and for each test case, it reads the number of monsters, the maximum number of bullets that can be used, the health of each monster, and the position of each monster. It then simulates the battle, using the minimum number of bullets necessary to defeat each monster, and checks if the total number of bullets used exceeds the maximum allowed. If it does, it prints 'NO', indicating that it is not possible to defeat all monsters. Otherwise, it prints 'YES'. The function repeats this process for each test case.

