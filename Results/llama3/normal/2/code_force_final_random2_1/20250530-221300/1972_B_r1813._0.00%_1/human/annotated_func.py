#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 100) followed by t test cases. Each test case contains an integer n (1 <= n <= 100) followed by a string s of length n containing only "U" and "D".
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
        
    #State: t is an integer equal to 0, data is a list of strings, index is equal to 2t + 1, _ is equal to t - 1, n is an integer equal to the value of data[2t - 1], s is a string equal to the value of data[2t], and num_up_coins is an integer equal to the number of 'U' characters in s. If num_up_coins is odd, results is a list containing t 'YES' strings. If num_up_coins is even, results is a list containing t 'NO' strings.
    for result in results:
        print(result)
        
    #State: `t` is 0, `data` is a list of strings, `index` is 1, `_` is -1, `n` is an integer equal to the value of data[-1], `s` is a string equal to the value of data[0], `num_up_coins` is an odd integer, `results` is an empty list, and no strings are being printed.

#Overall this is what the function does:Reads input from stdin, processes multiple test cases, and prints 'YES' or 'NO' for each case based on whether the number of 'U' characters in a given string is odd or even.

