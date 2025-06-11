#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains a single integer n (1 <= n <= 500) — the size of the matrix a.
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        sum = 1
        
        for i in range(2, n + 1):
            sum += (i * i - (i - 1) * (i - 1)) * i
        
        print(sum, n + n)
        
        for j in range(1, n + 1):
            print(1, n - j + 1, *range(1, n + 1))
            print(2, n - j + 1, *range(1, n + 1))
        
    #State: The loop will execute 't' times, each time taking an integer 'n' as input and printing the sum of squares of numbers from 1 to 'n' along with 'n + n', followed by 'n' lines of output with '1' and 'n - j + 1' (where 'j' ranges from 1 to 'n') and a list of numbers from 1 to 'n', and then another 'n' lines of output with '2' and 'n - j + 1' (where 'j' ranges from 1 to 'n') and a list of numbers from 1 to 'n'. The value of 't' will remain unchanged as it is not modified within the loop.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case contains a single integer 'n' representing the size of a matrix. For each test case, it calculates and prints the sum of squares of numbers from 1 to 'n' along with 'n + n'. Then, it prints 'n' lines of output with '1' and 'n - j + 1' (where 'j' ranges from 1 to 'n') followed by a list of numbers from 1 to 'n', and another 'n' lines of output with '2' and 'n - j + 1' (where 'j' ranges from 1 to 'n') followed by a list of numbers from 1 to 'n'. The function does not return any value but modifies the standard output based on the input test cases.

