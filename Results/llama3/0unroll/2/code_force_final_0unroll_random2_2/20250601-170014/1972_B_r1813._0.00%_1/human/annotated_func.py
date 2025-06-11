#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer (1 <= integer <= 100) and then a string of length integer containing only "U" and "D".
    input = sys.stdin.read
    data = input().split()
    index = 0
    t = int(data[index])
    index += 1
    results = []
    for _ in range(t):
        n = int(data[index])
        
        index += 1
        
        s = data[index]
        
        index += 1
        
        num_up_coins = s.count('U')
        
        if num_up_coins % 2 == 1:
            results.append('YES')
        else:
            results.append('NO')
        
    #State: Output State: The loop has executed t times, and the results list contains t boolean values indicating whether the number of 'U' coins in each test case is odd or even. The index variable has been incremented by 2t, and the stdin remains empty.
    for result in results:
        print(result)
        
    #State: Output State: The loop has executed t times, and the results list contains t boolean values indicating whether the number of 'U' coins in each test case is odd or even. The index variable has been incremented by 2t, and the stdin remains empty.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer and a string of that length containing only 'U' and 'D' characters. It then determines whether the number of 'U' characters in each string is odd or even and prints 'YES' for odd counts and 'NO' for even counts. The function processes all test cases and prints the results in the order they were received.

