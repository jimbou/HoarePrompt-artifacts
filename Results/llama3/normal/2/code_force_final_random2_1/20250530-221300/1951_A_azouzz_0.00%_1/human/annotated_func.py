#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer (between 1 and 1000) and then a binary string of the same length as the integer.
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        s = input()
        
        cnt1 = s.count('1')
        
        if cnt1 > 2 and cnt1 % 2 == 0:
            print('YES')
        elif cnt1 > 2 and (cnt1 % 2 == 1 or cnt1 == 1):
            print('NO')
        elif '11' in s:
            print('NO')
        else:
            print('YES')
        
    #State: t is 0, n is an integer equal to the input value, s is a binary string of the same length as n, cnt1 is the number of '1's in s, stdin contains no test cases. If cnt1 > 2 and cnt1 is even, 'YES' is printed. If cnt1 > 2 and cnt1 is odd or cnt1 is 1, 'NO' is printed. If '11' is in s, 'NO' is printed. Otherwise, 'YES' is printed.

#Overall this is what the function does:Determines whether a given binary string meets certain conditions and prints 'YES' or 'NO' accordingly. The function accepts multiple test cases from standard input, where each test case consists of an integer and a binary string of the same length. It counts the number of '1's in the binary string and checks if the count is greater than 2 and even, or if the string contains consecutive '1's. Based on these conditions, it prints 'YES' or 'NO' for each test case.

