#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first a positive integer (1 <= n <= 100) and then a string of length n containing only "U" and "D".
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
        
    #State: index is equal to 2t+1, results is a list of strings containing 'YES' if the count of 'U' in the corresponding string is odd, otherwise 'NO'.
    for result in results:
        print(result)
        
    #State: index is equal to 2t+1, results is a list of strings containing 'YES' if the count of 'U' in the corresponding string is odd, otherwise 'NO', results must have at least n results, result is the nth result in the list, and the nth result in the list which is either 'YES' or 'NO' is printed, and the result which is either 'YES' or 'NO' is printed

#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of a positive integer (n) and a string of length n containing only "U" and "D". It then determines whether the count of "U" in each string is odd or even and prints "YES" if it's odd, and "NO" if it's even, for each test case. The function processes all test cases and prints the corresponding results.

