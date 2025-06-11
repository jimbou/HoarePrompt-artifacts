#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer (1 <= integer <= 100) and then a string of length integer containing only "U" and "D".
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
        
    #State: The loop has executed t times, and the output is a series of 'YES' or 'NO' depending on whether the count of 'U' in each string s is odd or even. The value of index is now index + 2*t. The value of t is now 0. The value of data remains unchanged.

#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of an integer and a string of that length containing only 'U' and 'D' characters. It then checks each string to determine if the count of 'U' characters is odd or even, printing 'YES' if the count is odd and 'NO' if the count is even. The function processes all test cases and produces a series of 'YES' or 'NO' outputs accordingly.

