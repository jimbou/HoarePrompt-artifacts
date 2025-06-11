#State of the program right berfore the function call: stdin contains t test cases. Each test case contains two inputs: first an integer n and then a string s of length n. 1 <= t <= 10^4 and 1 <= n <= 10^6. The sum of n over all test cases does not exceed 10^6.
    for _ in range(int(input())):
        a = int(input())
        
        s = input()
        
        x = s.count('map')
        
        y = s.count('pie')
        
        print(x + y)
        
    #State: The number of occurrences of 'map' and 'pie' in each string s are counted and their sum is printed for each test case. The input state remains unchanged, with stdin containing the same test cases, each with an integer n and a string s of length n.

#Overall this is what the function does:Counts and prints the total occurrences of 'map' and 'pie' in each string s for multiple test cases, leaving the input state unchanged.

