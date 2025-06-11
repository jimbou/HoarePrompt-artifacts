#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t lines, each containing two space-separated integers a and b (1 <= a, b <= 10^9).
    t = int(input())
    for i in range(t):
        s = input()
        
        a = int(list(s.split())[0])
        
        b = int(list(s.split())[1])
        
        if (a + b) % 2 == 0:
            print('Bob')
        else:
            print('Alice')
        
    #State: The output will be a series of 'Bob' or 'Alice' printed to the console, with the number of lines equal to the value of t. Each line will be either 'Bob' or 'Alice', depending on whether the sum of the two integers on the corresponding line of stdin is even or odd, respectively. The value of t remains unchanged.

#Overall this is what the function does:The function reads an integer t from standard input, representing the number of test cases, and then reads t lines of input, each containing two space-separated integers a and b. It then prints 'Bob' if the sum of a and b is even, and 'Alice' if the sum is odd, for each test case. The function does not modify the input values or return any values, but instead prints the results directly to the console.

