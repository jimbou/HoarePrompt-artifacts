#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case consists of an integer n (2 <= n <= 2 * 10^5) followed by two strings of length n consisting of '<' and '>' characters. n is even.
    for _ in range(int(input())):
        n = int(input())
        
        a = list(map(str, input()))
        
        b = list(map(str, input()))
        
        if b[n - 2] == str('<'):
            print('No')
        else:
            print('Yes')
        
    #State: _ is t-1, stdin is empty. If the second last element of b is '<', then 'No' is printed. Otherwise, 'Yes' is printed.

#Overall this is what the function does:Determines whether a given pair of strings of '<' and '>' characters can be rearranged to form a valid sequence, and prints 'Yes' or 'No' accordingly.

