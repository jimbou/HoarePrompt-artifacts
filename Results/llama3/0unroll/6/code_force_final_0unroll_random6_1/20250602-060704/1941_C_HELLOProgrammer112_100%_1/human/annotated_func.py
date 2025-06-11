#State of the program right berfore the function call: stdin contains t test cases. Each test case contains two inputs: first an integer n and then a string s of length n. 1 <= t <= 10^4, 1 <= n <= 10^6. The sum of n over all test cases does not exceed 10^6.
    for _ in range(int(input())):
        a = int(input())
        
        s = input()
        
        x = s.count('map')
        
        y = s.count('pie')
        
        z = s.count('mapie')
        
        print(x + y - z)
        
    #State: The output state will be the sum of the counts of 'map' and 'pie' minus the count of 'mapie' for each test case, printed on separate lines. The number of lines will be equal to the number of test cases t. The input string s and its length n will not be modified.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer n and a string s of length n. It then counts the occurrences of the substrings 'map', 'pie', and 'mapie' in the string s, and prints the sum of the counts of 'map' and 'pie' minus the count of 'mapie' for each test case. The function does not modify the input string s or its length n. The output is a series of integers, one for each test case, representing the calculated sum.

