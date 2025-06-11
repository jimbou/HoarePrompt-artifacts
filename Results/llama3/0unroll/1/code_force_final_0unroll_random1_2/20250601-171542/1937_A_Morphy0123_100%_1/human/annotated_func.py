#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains an integer t (1 <= t <= 10^4), representing the number of test cases. Each of the following t lines contains a single integer n (1 <= n <= 10^9), representing the length of the array a.
    n_cases = int(input())
    for i in range(n_cases):
        n = int(input())
        
        if n == 1:
            print(1)
        else:
            power = 1
            n = log2(n)
            while power < n:
                power += 1
            if power == n:
                print(2 ** power)
            else:
                power -= 1
                print(2 ** power)
        
    #State: The output state will contain `n_cases` lines of output, each containing a single integer. For each input integer `n`, if `n` is 1, the output will be 1. Otherwise, the output will be the largest power of 2 that is less than or equal to `n`.

#Overall this is what the function does:The function reads multiple lines of input from stdin, where the first line contains the number of test cases (t) and each subsequent line contains a single integer (n). It then processes each integer n, printing the largest power of 2 that is less than or equal to n if n is not 1, and 1 if n is 1. The function outputs t lines, each containing a single integer, representing the results of the power of 2 calculations for each input integer n.

