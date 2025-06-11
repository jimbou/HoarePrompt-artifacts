#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains one input: an integer n (1 <= n <= 500).
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
        
    #State: `n` is an integer greater than or equal to 0, `i` is 0, `mat` is a square matrix of size `n` x `n` with values ranging from 1 to `n`, `res` is the sum of the first `n` cubes, `stdin` contains no test cases, `_` is equal to the number of test cases, the sum of the first `n` cubes which is `res` and the value of `n` left shifted by 1 (i.e., `n` multiplied by 2) are printed, and the number 1 followed by the value of `i` (which is 0) and the numbers from 1 to `n` are being printed, and the number 2 followed by the value of `i` (which is 0) and the numbers from 1 to `n` are being printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case contains a single integer n. For each test case, it calculates the sum of the first n cubes, prints this sum along with the value of n multiplied by 2, and then prints a series of numbers in a specific pattern. The function does not return any value but instead prints the results directly to the console.

