#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case consists of an integer n (1 <= n <= 10^6) followed by a string s of length n consisting of lowercase Latin letters.
    for _ in range(int(input())):
        a = int(input())
        
        s = input()
        
        x = s.count('map')
        
        y = s.count('pie')
        
        z = s.count('mapie')
        
        print(x + y - z)
        
    #State: a is an integer equal to the input value, s is a string equal to the input string, x is the number of occurrences of 'map' in s, y is the number of occurrences of 'pie' in s, z is the number of occurrences of 'mapie' in s, _ is t-1, t is 0, stdin contains 0 test cases, and the sum of the number of occurrences of 'map' and 'pie' minus the number of occurrences of 'mapie' in the string s is printed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer n followed by a string s of length n. It then counts the occurrences of the substrings 'map', 'pie', and 'mapie' in the string s, and prints the sum of the counts of 'map' and 'pie' minus the count of 'mapie'. The function processes all test cases and prints the result for each case.

