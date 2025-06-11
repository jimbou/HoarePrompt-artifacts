#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case contains an integer n (2 <= n <= 2 * 10^5) followed by two strings of length n consisting of '<' and '>' characters. The sum of n over all test cases does not exceed 2 * 10^5.
    for _ in range(int(input())):
        n = int(input())
        
        a = list(map(str, input()))
        
        b = list(map(str, input()))
        
        if b[n - 2] == str('<'):
            print('No')
        else:
            print('Yes')
        
    #State: The output state will be a series of 'Yes' or 'No' printed to the console, one for each test case. The output will indicate whether the second last character of the second string is '>' or '<' respectively. The input state remains unchanged, with the same values for t, n, a, and b as in the initial state.

#Overall this is what the function does:This function reads input from the standard input, processes it, and prints output to the console. It accepts no parameters and returns no values. The function reads an integer t, representing the number of test cases, followed by t test cases. Each test case consists of an integer n and two strings a and b of length n, containing '<' and '>' characters. The function then checks the second last character of the second string b and prints 'Yes' if it is '>' and 'No' if it is '<'. The function does not modify the input state and only prints output to the console.

