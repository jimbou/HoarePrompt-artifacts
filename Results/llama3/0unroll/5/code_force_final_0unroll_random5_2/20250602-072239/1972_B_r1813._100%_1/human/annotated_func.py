#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer (1 <= n <= 100) and then a string of length n containing only "U" and "D".
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
        
    #State: Output State: The loop has executed t times, index is now 2t + 1, and stdin remains unchanged. The loop has printed 'YES' or 'NO' t times, depending on the count of 'U's in each string s.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer and a string of 'U's and 'D's. It then determines whether the count of 'U's in each string is odd or even and prints 'YES' if odd and 'NO' if even, repeating this process for each test case. The function does not modify the input or standard input stream.

