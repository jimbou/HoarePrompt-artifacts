#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer (1 <= t <= 1000) and then a binary string of size n (1 <= n <= 50).
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
        
    #State: The loop will have printed 'YES' or 'NO' for each test case, indicating whether the binary string can be rearranged into a palindrome or not, based on the count of '1's and the presence of consecutive '1's. The value of `t` will be unchanged, and the contents of stdin will be consumed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer and a binary string. It then checks if the binary string can be rearranged into a palindrome based on the count of '1's and the presence of consecutive '1's, printing 'YES' if possible and 'NO' otherwise. The function processes all test cases and consumes the contents of standard input, leaving the value of the initial integer unchanged.

