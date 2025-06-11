#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer (1 <= n <= 50) and then a binary string of size n.
    t = int(input())
    for i in range(t):
        n = int(input())
        
        a = input()
        
        count = a.count('1')
        
        if count == 0:
            print('YES')
        elif count > 2 and count % 2 == 0:
            print('YES')
        elif count == 2:
            if a.index('1') and a[a.index('1') + 1] != '1':
                print('YES')
            else:
                print('NO')
        else:
            print('NO')
        
    #State: The loop will execute 't' number of times, where 't' is an integer between 1 and 50. In each iteration, it will read an integer 'n' and a binary string 'a' of size 'n' from the standard input. It will then count the number of '1's in the string 'a' and store it in the variable 'count'. If 'count' is 0, it will print 'YES'. If 'count' is greater than 2 and even, it will print 'YES'. If 'count' is 2, it will check if the first '1' in the string 'a' is not followed by another '1', and if so, it will print 'YES', otherwise it will print 'NO'. In all other cases, it will print 'NO'. The loop will not modify the value of 't' or any other variables outside the loop.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer 'n' and a binary string 'a' of size 'n'. It then checks the number of '1's in the string 'a' and prints 'YES' or 'NO' based on the following conditions: if there are no '1's, if there are more than 2 '1's and the count is even, or if there are exactly 2 '1's and they are not consecutive. In all other cases, it prints 'NO'. The function processes 't' number of test cases, where 't' is an integer between 1 and 50, and does not modify any external variables.

