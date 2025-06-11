#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains one input: an integer (between 1 and 500 inclusive).
    for _ in range(int(input())):
        n = int(input())
        
        mat = [list(range(1, n + 1)) for i in range(n)]
        
        res = 0
        
        for i in range(n):
            res += (i + 1) * (2 * i + 1)
        
        print(res, n << 1)
        
        for i in range(n, 0, -1):
            print('1 %d' % i, *range(1, n + 1))
            print('2 %d' % i, *range(1, n + 1))
        
    #State: `n` is an integer at least 1, `mat` is a 2D list of size `n` x `n` where each row contains consecutive integers from 1 to `n`, `res` is the sum of (i + 1) * (2 * i + 1) for i from 0 to `n` - 1, `i` is 0, `stdin` is empty, the sum of (i + 1) * (2 * i + 1) for i from 0 to `n` - 1 which is equal to `res` and the value of `n` left shifted by 1 which is equal to `n` * 2 is printed for each test case, '1 %d' % i, *range(1, n + 1) is printed for each `i` from `n` to 1 for each test case, and '2 %d' % i, *range(1, n + 1) is printed for each `i` from `n` to 1 for each test case.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case contains a single integer between 1 and 500 inclusive. For each test case, it calculates the sum of (i + 1) * (2 * i + 1) for i from 0 to n - 1, prints this sum along with the value of n multiplied by 2, and then prints two sets of numbers from 1 to n for each i from n to 1. After processing all test cases, the function leaves the standard input empty.

