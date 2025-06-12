#State of the program right berfore the function call: stdin contains two inputs: first an integer (t) representing the number of test cases, and then for each test case, two integers (n and k) separated by a space, where 1 <= k <= n <= 10^3.
    for s in [*open(0)][1:]:
        n, k = map(int, s.split())
        
        if k >= 2:
            if n == k:
                print(*[k for j in range(k)])
            else:
                print('-1')
        else:
            print(*[j for j in range(n)])
        
    #State: `n` and `k` are the last pair of integers from the input, `s` is the last line of the file object, stdin is empty. If `k` is greater than or equal to 2, then if `n` is equal to `k`, `k` repeated `k` times is printed for each test case where this condition is met, otherwise -1 is printed for each test case where this condition is met. If `k` is less than 2, the numbers from 0 to n-1 are printed for each test case where this condition is met.

#Overall this is what the function does:This function reads input from stdin, processes multiple test cases, and prints output based on the values of `n` and `k`. For each test case, if `k` is 1, it prints numbers from 0 to `n-1`. If `k` is greater than or equal to 2, it checks if `n` is equal to `k`, printing `k` repeated `k` times if true, and -1 otherwise. After processing all test cases, the function leaves `n` and `k` as the last pair of integers from the input, `s` as the last line of the file object, and stdin empty.

