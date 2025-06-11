#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of two lines. The first line contains four integers n, f, a, and b. The second line contains n integers m_1, m_2, \dots, m_n. 1 <= n <= 2 * 10^5, 1 <= f, a, b <= 10^9, 1 <= m_i <= 10^9, and m_i < m_{i + 1}.
    t = int(input())
    for _ in range(t):
        n, f, a, b = map(int, input().split())
        
        arr = [0] + list(map(int, input().split()))
        
        possible = True
        
        for i in range(1, n + 1):
            time_diff = arr[i] - arr[i - 1]
            energy_keep_on = a * time_diff
            energy_turn_off_on = b
            energy_cost = min(energy_keep_on, energy_turn_off_on)
            if f <= energy_cost:
                possible = False
                break
            f -= energy_cost
        
        print('YES' if possible else 'NO')
        
    #State: `t` is 0, `_` is `t`, `n`, `f`, `a`, `b`, `arr`, and `possible` are undefined, and either 'YES' or 'NO' has been printed for each test case.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two lines. The first line contains four integers: n, f, a, and b. The second line contains n integers: m_1, m_2, ..., m_n. The function then determines whether it is possible to keep a device on given the energy costs of keeping it on versus turning it off and on again. If the device can be kept on, it prints 'YES', otherwise it prints 'NO'. The function repeats this process for each test case.

