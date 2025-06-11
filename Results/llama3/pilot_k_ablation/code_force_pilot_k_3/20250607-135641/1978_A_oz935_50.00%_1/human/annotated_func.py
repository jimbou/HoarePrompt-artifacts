#State of the program right berfore the function call: stdin contains an integer t (1 ≤ t ≤ 500) followed by t test cases. Each test case contains an integer n (2 ≤ n ≤ 100) followed by n integers a_1, a_2, …, a_n (1 ≤ a_i ≤ 10^9).
    t = int(input().strip())
    for i in range(t):
        n = int(input().strip())
        
        ls = input().split()
        
        last = int(ls.pop())
        
        other = int(sorted(ls).pop())
        
        print(last + other)
        
    #State: t is an integer between 1 and 500, i is t-1, stdin is empty, n is an integer between 2 and 100, last is an integer between 1 and 10^9, other is an integer between 1 and 10^9, and the sum of last and other is being printed, which is an integer between 2 and 2*10^9.

#Overall this is what the function does:This function reads input from stdin, processes it, and prints output. It accepts no parameters and returns no value. It reads an integer t, representing the number of test cases, and then for each test case, it reads an integer n and n integers. It then prints the sum of the last integer and the second-largest integer in the list. The function modifies the state of stdin by consuming all input and leaves it empty. The function's purpose is to solve a specific problem by processing input and producing output based on that input.

