#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t lines, each containing two integers a and b (1 <= a, b <= 10^9).
    t = int(input())
    for i in range(t):
        s = input()
        
        a = int(list(s.split())[0])
        
        b = int(list(s.split())[1])
        
        if (a + b) % 2 == 0:
            print('Bob')
        else:
            print('Alice')
        
    #State: The output state will contain t lines, each containing either 'Bob' or 'Alice'. The value on each line is determined by whether the sum of the two integers on the corresponding line in the input is even ('Bob') or odd ('Alice'). The value of t remains unchanged.

#Overall this is what the function does:Determines the winner ('Alice' or 'Bob') for each of t pairs of integers based on whether their sum is odd or even, and prints the results.

