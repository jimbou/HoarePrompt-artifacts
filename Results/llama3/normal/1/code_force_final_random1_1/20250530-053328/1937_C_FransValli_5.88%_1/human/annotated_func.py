#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains an integer n (2 <= n <= 10^4) followed by a permutation p of integers from 0 to n - 1.
    for _ in range(int(input())):
        n = int(input())
        
        k = 1
        
        for i in range(2, n):
            print('?', 0, k, 0, i, flush=True)
            res = input()
            if res == '<':
                k = i
        
        best = 0
        
        for i in range(1, n):
            print('?', k, best, k, i, flush=True)
            res = input()
            if res == '<':
                best = i
        
        print('!', k, best, flush=True)
        
    #State: `n` is a positive integer greater than its original value, `i` is `n`, `res` is either '<' or not '<', `k` is `n-1` if `res` is '<' otherwise `k` is `n-2`, `best` is `n-1` if `res` is '<' otherwise `best` is 0, stdin contains at least 0 test case, and '?' followed by the value of `k` which is either `n-1` or `n-2` depending on the value of `res`, followed by the value of `best` which is either `n-1` or 0 depending on the value of `res`, followed by the value of `k` again, and finally followed by the value of `i` which is `n` has been printed, and this is printed: '!' followed by the value of `k` which is either `n-1` or `n-2` depending on the value of `res`, followed by the value of `best` which is either `n-1` or 0 depending on the value of `res`.

#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case contains an integer n followed by a permutation of integers from 0 to n-1. For each test case, it finds the maximum and second maximum elements in the permutation and prints them in the format '! k best', where k is the maximum element and best is the second maximum element. The function also prints intermediate queries in the format '? k best k i' to determine the maximum and second maximum elements.

