#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t test cases. Each test case consists of an integer n (1 <= n <= 20) followed by three strings a, b, c, each consisting of n lowercase Latin letters.
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = input().strip()
        
        b = input().strip()
        
        c = input().strip()
        
        possible = False
        
        for i in range(n):
            if a[i] == b[i]:
                if c[i] != a[i]:
                    possible = True
                    break
            elif c[i] == a[i] or c[i] == b[i]:
                continue
            else:
                possible = True
                break
        
        if possible:
            print('YES')
        else:
            print('NO')
        
    #State: The output state will be a series of 'YES' or 'NO' printed to the console, each corresponding to whether it is possible to make the strings a, b, and c identical by changing one or more characters in a and b, but not in c. The number of 'YES' or 'NO' printed will be equal to the value of t.

#Overall this is what the function does:This function reads input from the standard input, processes multiple test cases, and prints 'YES' or 'NO' to the console for each test case. The function determines whether it is possible to make three input strings identical by changing one or more characters in the first two strings, but not in the third string. The function processes a specified number of test cases, and the output is a series of 'YES' or 'NO' responses, one for each test case.

