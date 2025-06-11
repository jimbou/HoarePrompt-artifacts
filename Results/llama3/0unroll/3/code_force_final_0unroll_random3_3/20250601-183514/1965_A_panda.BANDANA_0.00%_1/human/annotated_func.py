#State of the program right berfore the function call: stdin contains t test cases. Each test case contains two inputs: first an integer n and then n integers. n is a positive integer and each of the n integers is a positive integer.
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
        
    #State: The output state is a series of 'Alice' or 'Bob' printed to the console, with the number of lines equal to the initial value of t. Each line is determined by whether the number 1 is present in the corresponding list of integers. If 1 is present, 'Bob' is printed; otherwise, 'Alice' is printed. The value of t is not changed, and the input test cases are consumed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of a positive integer n followed by n positive integers. It then checks if the number 1 is present in each list of integers and prints 'Bob' if 1 is present, or 'Alice' if 1 is not present. The function prints a series of 'Alice' or 'Bob' lines to the console, with the number of lines equal to the initial number of test cases.

