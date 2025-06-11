#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case consists of an integer n (1 <= n <= 10^6) followed by a string s of length n consisting of lowercase Latin letters.
    for _ in range(int(input())):
        a = int(input())
        
        s = input()
        
        x = s.count('map')
        
        y = s.count('pie')
        
        print(x + y)
        
    #State: The output state will contain t number of lines, each containing the sum of occurrences of 'map' and 'pie' in the corresponding string s. The input integer t and the strings s remain unchanged.

#Overall this is what the function does:This function reads input from standard input, processes it, and prints output to standard output. It accepts no parameters and returns no value. The function reads an integer t, followed by t test cases, each consisting of an integer n and a string s. For each test case, it counts the occurrences of the substrings 'map' and 'pie' in the string s and prints their sum. The input values of t and the strings s remain unchanged. The function produces t lines of output, each containing the sum of 'map' and 'pie' occurrences for the corresponding test case.

