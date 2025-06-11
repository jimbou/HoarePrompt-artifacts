#State of the program right berfore the function call: stdin contains multiple inputs: first an integer t (1 <= t <= 10^4), then for each test case, first an integer n (2 <= n <= 2 * 10^5) and then two strings of length n consisting of '<' and/or '>' characters.
    for _ in range(int(input())):
        n = int(input())
        
        a = list(map(str, input()))
        
        b = list(map(str, input()))
        
        if b[n - 2] == str('<'):
            print('No')
        else:
            print('Yes')
        
    #State: The output state will contain 'Yes' or 'No' for each test case, depending on whether the second last character of the second string is '>' or '<' respectively. The number of 'Yes' or 'No' will be equal to the number of test cases (t).

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer n and two strings of length n containing '<' and '>' characters. It then checks the second last character of the second string in each test case and prints 'Yes' if it is '>' and 'No' if it is '<'. The function repeats this process for the number of test cases specified at the beginning of the input.

