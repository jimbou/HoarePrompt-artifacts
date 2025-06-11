#State of the program right berfore the function call: stdin contains t test cases. Each test case contains two inputs: first an integer n (1 <= n <= 10^6) and then a string s of length n consisting of lowercase Latin letters.
    for _ in range(int(input())):
        a = int(input())
        
        s = input()
        
        x = s.count('map')
        
        y = s.count('pie')
        
        z = s.count('mapie')
        
        print(x + y - z)
        
    #State: The output will be the sum of the counts of 'map' and 'pie' minus the count of 'mapie' for each test case, printed on separate lines.

#Overall this is what the function does:The function reads a series of test cases from standard input, where each test case consists of an integer n and a string s of length n. It then counts the occurrences of the substrings 'map', 'pie', and 'mapie' in the string s, and prints the sum of the counts of 'map' and 'pie' minus the count of 'mapie' for each test case.

