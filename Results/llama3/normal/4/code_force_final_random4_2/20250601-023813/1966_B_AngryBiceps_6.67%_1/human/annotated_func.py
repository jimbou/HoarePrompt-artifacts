#State of the program right berfore the function call: stdin contains a sequence of lines. The first line contains a single integer t (1 <= t <= 10^4). Each of the next t blocks of lines contains: a line with two integers n and m (1 <= n, m <= 500), followed by n lines each containing m characters 'W' and 'B'.
    for _ in range(int(input())):
        n, m = map(int, input().split())
        
        a = []
        
        first_row = ''
        
        last_row = ''
        
        for i in range(n):
            a.append(input())
            first_row += a[-1][0]
            last_row += a[-1][-1]
        
        if len(set(a[0])) == 1 and a[0] != a[-1]:
            print('NO')
        elif len(set(first_row)) == 1 and first_row != last_row:
            print('NO')
        else:
            print('YES')
        
    #State: n is an integer, m is an integer, i is n-1, a is a list containing n strings, first_row is a string of n characters, last_row is a string of n characters, _ is t-1, stdin contains an empty sequence of lines. If the first string in the list a contains only one unique character and is not equal to the last string in the list a, then 'NO' is printed. Otherwise, 'YES' is printed.

#Overall this is what the function does:This function reads a sequence of lines from standard input, where the first line contains an integer t, representing the number of test cases. For each test case, it reads two integers n and m, followed by n lines of m characters each. It then checks if the first row of characters is uniform and different from the last row, or if the first column of characters is uniform and different from the last column. If either condition is true, it prints 'NO', otherwise it prints 'YES'. The function repeats this process for all test cases and leaves the standard input empty.

