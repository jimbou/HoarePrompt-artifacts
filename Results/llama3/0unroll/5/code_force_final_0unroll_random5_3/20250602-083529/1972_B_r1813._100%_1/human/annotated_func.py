#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 100) followed by t test cases. Each test case contains an integer n (1 <= n <= 100) followed by a string s of length n containing only "U" and "D".
    input = sys.stdin.read
    data = input().split()
    t = int(data[0])
    index = 1
    for _ in range(t):
        n = int(data[index])
        
        s = data[index + 1]
        
        index += 2
        
        count_u = s.count('U')
        
        if count_u % 2 == 1:
            print('YES')
        else:
            print('NO')
        
    #State: The loop has executed t times, printing either 'YES' or 'NO' for each iteration. The value of index has been incremented by 2t. The values of stdin, t, and data remain unchanged.

#Overall this is what the function does:This function reads input from standard input, processes it, and prints output. It reads an integer t, representing the number of test cases, followed by t test cases. Each test case consists of an integer n and a string s of length n containing only "U" and "D". The function then counts the number of "U"s in each string and prints "YES" if the count is odd, and "NO" if it's even. After processing all test cases, the function concludes, leaving the input variables unchanged.

