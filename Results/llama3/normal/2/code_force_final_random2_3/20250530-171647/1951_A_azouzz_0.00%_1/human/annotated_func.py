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
        
    #State: t is an integer between 1 and 1000 and equal to 0, _ is equal to the initial value of t, n is an integer equal to the value of the input, s is a binary string of the same length as t, cnt1 is an integer equal to the number of '1's in s, stdin contains no test cases. If cnt1 is greater than 2 and cnt1 is even, 'YES' is printed. If cnt1 is greater than 2 and cnt1 is odd or cnt1 is 1, 'NO' is printed. Otherwise, if '11' is in s, 'NO' is printed. Otherwise, 'YES' is printed.

#Overall this is what the function does:This function processes multiple test cases from standard input, where each test case consists of an integer and a binary string of the same length. It counts the number of '1's in the binary string and prints 'YES' or 'NO' based on the count and the presence of consecutive '1's in the string. The function iterates through all test cases and prints the corresponding results.

