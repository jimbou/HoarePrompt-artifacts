#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case contains two lines. The first line contains four integers n, f, a, and b (1 <= n <= 2 * 10^5, 1 <= f, a, b <= 10^9). The second line contains n integers m_1, m_2, ..., m_n (1 <= m_i <= 10^9, m_i < m_{i+1}).
    t = int(input(''))
    while t > 0:
        n, f, a, b = map(int, input('').split(' '))
        
        ls = list(map(int, input('').split(' ')))
        
        for i in range(1, len(ls)):
            f = f - min(a * (ls[i] - ls[i - 1]), b)
        
        if f > 0:
            print('YES')
        else:
            print('NO')
        
        t -= 1
        
    #State: t = 0, f = 0, n = 0, a = 0, b = 0, ls = []

#Overall this is what the function does:This function reads input from stdin, processes multiple test cases, and determines whether a given amount of fuel is sufficient to cover a sequence of distances. It iterates through each test case, calculating the remaining fuel after traversing the distances, and prints 'YES' if the fuel is sufficient and 'NO' otherwise. The function continues processing test cases until all inputs have been exhausted.

