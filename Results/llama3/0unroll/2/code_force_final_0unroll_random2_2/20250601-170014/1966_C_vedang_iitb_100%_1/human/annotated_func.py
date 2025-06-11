#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer n (1 <= n <= 2*10^5) and then n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^9). The number of test cases is between 1 and 10^4.
    t = int(input())
    for tc in range(t):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        maxsize = max(a)
        
        a.sort()
        
        mexsize = 1
        
        for sz in a:
            if sz == mexsize:
                mexsize = mexsize + 1
        
        if mexsize > maxsize:
            print('Alice' if mexsize % 2 == 0 else 'Bob')
        else:
            print('Alice' if mexsize % 2 == 1 else 'Bob')
        
    #State: The output state will be a list of strings, where each string is either 'Alice' or 'Bob', depending on the value of mexsize and maxsize for each test case. The number of strings in the list will be equal to the value of t. The stdin will be empty after the loop executes all the iterations.

#Overall this is what the function does:Determines the winner ('Alice' or 'Bob') for each test case based on the minimum excluded size (mexsize) and maximum size (maxsize) of a sorted list of integers, and prints the results.

