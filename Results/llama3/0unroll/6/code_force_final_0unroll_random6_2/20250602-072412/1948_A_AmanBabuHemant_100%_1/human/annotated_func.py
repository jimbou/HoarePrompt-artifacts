#State of the program right berfore the function call: stdin contains two inputs: first an integer t (1 <= t <= 50) and then t integers n (1 <= n <= 50).
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        if n % 2:
            print('NO')
        else:
            s = 'AAB' * (n // 2)
            if len(s) < 200:
                print('YES')
                print(s)
            else:
                print('NO')
        
    #State: The output state is a series of 'YES' or 'NO' responses, followed by a string of 'AAB' repeated a certain number of times, depending on the input values. The number of responses is equal to the initial value of t. For each input value n, if n is even, the response is 'YES' followed by a string of 'AAB' repeated n/2 times, as long as the length of the string is less than 200. If n is odd or the length of the string is 200 or more, the response is 'NO'.

#Overall this is what the function does:This function reads a series of integers from standard input, where the first integer t represents the number of subsequent integers. For each subsequent integer n, the function checks if n is even and if the length of the string 'AAB' repeated n/2 times is less than 200. If both conditions are met, it prints 'YES' followed by the repeated string; otherwise, it prints 'NO'. The function repeats this process t times, providing a series of 'YES' or 'NO' responses along with the corresponding strings.

