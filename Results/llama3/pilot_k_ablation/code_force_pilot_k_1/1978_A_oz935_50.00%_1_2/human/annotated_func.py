#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer (the number of books Alice has) and then a space-separated list of integers (the number of pages in each book). The number of books is a non-negative integer and the number of pages in each book is a positive integer.
    t = int(input().strip())
    for i in range(t):
        n = int(input().strip())
        
        ls = input().split()
        
        last = int(ls.pop())
        
        other = int(sorted(ls).pop())
        
        print(last + other)
        
    #State: `t` is a non-negative integer, `i` is `t`, `n` is an integer, `last` is an integer, `other` is an integer, stdin contains no test cases, each test case contains no space-separated list of integers, and the sum of `last` and `other` has been printed `t` times.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer (number of books) followed by a space-separated list of integers (number of pages in each book). It then calculates and prints the sum of the number of pages in the last book and the number of pages in the second-largest book for each test case. After processing all test cases, the function leaves the standard input empty.

