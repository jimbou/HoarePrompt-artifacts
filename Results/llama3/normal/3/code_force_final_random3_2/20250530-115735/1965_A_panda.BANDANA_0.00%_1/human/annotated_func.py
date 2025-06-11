#State of the program right berfore the function call: stdin contains t test cases. Each test case contains two inputs: first an integer n (1 <= n <= 2*10^5) and then a list of n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^9).
    t = int(input())
    for i in range(t):
        n = int(input())
        
        l = list(map(int, input().split()))
        
        e = set(l)
        
        m = len(l)
        
        if 1 in l:
            print('Bob')
        else:
            print('Alice')
        
    #State: t is an integer greater than or equal to 0, i is equal to t-1, n is an integer equal to the first input, l is a list of integers equal to the second input, e is a set of integers equal to the elements of l, m is an integer equal to the length of l, stdin contains 0 test cases. If 1 is in the list l, 'Bob' is printed. Otherwise, 'Alice' is printed.

#Overall this is what the function does:Determines the winner of a game based on the presence of the number 1 in a list of integers. The function reads input from stdin, processes multiple test cases, and prints 'Bob' if 1 is present in the list, otherwise prints 'Alice'.

