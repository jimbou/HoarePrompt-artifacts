#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains an integer n and m, followed by n strings of length m, consisting of characters 'W' and 'B'.
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
        
    #State: n is an integer greater than or equal to 0, m is an integer, a is a list containing n strings, first_row is a string consisting of the first character of each input string, last_row is a string consisting of the last character of each input string, i is n-1, stdin contains no input, _ is equal to the number of test cases. If the first string in the list a consists of only one unique character and the first string in the list a is not the same as the last string in the list a, then 'NO' is printed. If the first string in the list a consists of only one unique character and the first string in the list a is not the same as the last string in the list a, and the first_row is equal to the last_row, then 'NO' is printed. Otherwise, either the length of the set of characters in the first string of a is not equal to 1 or the first string of a is equal to the last string of a, and 'YES' is printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer n and m, followed by n strings of length m, containing characters 'W' and 'B'. It then checks each test case to determine if the first string is the same as the last string, and if the first row (first character of each string) is the same as the last row (last character of each string). If the first string consists of only one unique character and is not the same as the last string, or if the first row is the same as the last row but the first string is not the same as the last string, it prints 'NO'. Otherwise, it prints 'YES'. The function processes all test cases and prints the corresponding results.

