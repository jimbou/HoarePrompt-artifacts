#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case consists of an integer n (1 <= n <= 10^6) followed by a string s of length n consisting of lowercase Latin letters.
    for _ in range(int(input())):
        a = int(input())
        
        s = input()
        
        x = s.count('map')
        
        y = s.count('pie')
        
        z = s.count('mapie')
        
        print(x + y - z)
        
    #State: The output state will contain t lines, each containing the total count of 'map' and 'pie' substrings in the corresponding string s, minus the count of 'mapie' substrings. The input string s and the integer n will remain unchanged.

#Overall this is what the function does:This function reads input from stdin, processes multiple test cases, and prints the total count of 'map' and 'pie' substrings minus the count of 'mapie' substrings for each test case. It does not modify the input string or integer. The output consists of multiple lines, each containing the calculated count for a corresponding test case.

