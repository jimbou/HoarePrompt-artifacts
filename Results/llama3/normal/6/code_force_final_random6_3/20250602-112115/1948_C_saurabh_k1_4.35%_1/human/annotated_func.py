#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case contains an integer n (2 <= n <= 2 * 10^5) followed by two strings of length n consisting of '<' and '>' characters. n is even. The sum of n over all test cases doesn't exceed 2 * 10^5.
    for _ in range(int(input())):
        n = int(input())
        
        a = list(map(str, input()))
        
        b = list(map(str, input()))
        
        if b[n - 2] == str('<'):
            print('No')
        else:
            print('Yes')
        
    #State: n is an integer equal to the first input, a is a list of characters from the second input, b is a list of characters from the third input, _ is equal to the first input, stdin is empty. If the character at index n-2 in list b is '<', then 'No' is printed. Otherwise, 'Yes' is printed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer n and two strings of length n containing '<' and '>' characters. It then checks the character at the second-to-last position in the second string of each test case. If the character is '<', it prints 'No'; otherwise, it prints 'Yes'. The function processes all test cases and prints a corresponding 'No' or 'Yes' for each one.

