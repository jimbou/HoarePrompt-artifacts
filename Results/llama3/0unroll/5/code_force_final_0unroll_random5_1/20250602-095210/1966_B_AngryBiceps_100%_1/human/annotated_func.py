#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two integers n and m (1 <= n, m <= 500) and a grid of n x m characters 'W' and 'B'.
    for _ in range(int(input())):
        n, m = map(int, input().split())
        
        a = []
        
        first_row = ''
        
        last_row = ''
        
        for i in range(n):
            a.append(input())
            first_row += a[-1][0]
            last_row += a[-1][-1]
        
        if len(set(a[0])) == 1 and len(set(a[-1])) == 1 and a[0] != a[-1]:
            print('NO')
        elif len(set(first_row)) == 1 and len(set(last_row)
            ) == 1 and first_row != last_row:
            print('NO')
        else:
            print('YES')
        
    #State: The output state will contain a series of 'YES' or 'NO' strings, each corresponding to a test case. The output will indicate whether the given grid of characters 'W' and 'B' satisfies the conditions specified in the loop body.

#Overall this is what the function does:Determines whether a given grid of 'W' and 'B' characters satisfies specific conditions for each test case and outputs 'YES' or 'NO' accordingly.

