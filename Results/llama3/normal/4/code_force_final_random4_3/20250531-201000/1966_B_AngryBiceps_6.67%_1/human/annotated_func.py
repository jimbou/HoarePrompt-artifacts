#State of the program right berfore the function call: stdin contains t test cases. Each test case contains two integers n and m, followed by n strings of length m, each consisting of characters 'W' and 'B'.
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
        
    #State: n is an integer, m is an integer, a is a list containing n strings, first_row is a string of n characters, last_row is a string of n characters, _ is t-1, stdin is empty, i is n-1. If the first string in the list a contains only one unique character and the first string in the list a is not equal to the last string in the list a, then 'NO' is printed. Otherwise, if the length of the set of the first row is 1 and the first row is not equal to the last row, then 'NO' is printed. Otherwise, 'YES' is printed.

#Overall this is what the function does:This function reads input from stdin, processes it, and prints 'YES' or 'NO' based on certain conditions. It accepts no parameters and returns no value. The function iterates over a specified number of test cases, each containing a grid of characters 'W' and 'B'. It checks if the first row or the first column of the grid contains only one unique character and is not equal to the last row or column, respectively. If either condition is true, it prints 'NO'; otherwise, it prints 'YES'. The function modifies the input variables n, m, a, first_row, last_row, _, and i, and empties the stdin.

