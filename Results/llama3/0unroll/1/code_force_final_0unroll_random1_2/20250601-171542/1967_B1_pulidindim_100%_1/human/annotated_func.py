#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two positive integers n and m (1 <= n, m <= 2 * 10^6).
    t = int(input())
    for i in range(t):
        n, m = map(int, input().split())
        
        count = 2
        
        ans = n
        
        while count <= m:
            countmins = int(count - 1)
            g = int(n / count)
            if g < countmins:
                break
            g -= countmins
            ans += int(g / count) + 1
            count += 1
        
        print(int(ans))
        
    #State: The loop will execute t times, each time reading two positive integers n and m from stdin, and printing the calculated value of ans to stdout. The value of t will be decremented by 1 after each iteration, and will be 0 after the loop finishes. The value of n and m will be updated in each iteration with the new values read from stdin. The value of count will be reset to 2 in each iteration, and will be incremented by 1 in each iteration of the while loop until it exceeds m. The value of ans will be updated in each iteration of the while loop based on the values of n, count, and g. The value of g will be calculated in each iteration of the while loop based on the values of n and count. The value of countmins will be calculated in each iteration of the while loop based on the value of count.

#Overall this is what the function does:Calculates and prints the maximum number of integers that can be divided into 'n' parts, each part being at least 'countmins' (one less than the current divisor), for 't' test cases, where 'n' and 'm' are positive integers read from standard input, and 'm' is the maximum divisor.

