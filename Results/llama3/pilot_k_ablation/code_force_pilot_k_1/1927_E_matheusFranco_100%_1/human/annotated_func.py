#State of the program right berfore the function call: stdin contains two inputs: two space-separated integers n and k, where k is even and 2 <= k <= n <= 2 * 10^5.
    n, k = map(int, input().split(' '))
    permutation = [0] * n
    bottom_v = 1
    top_v = n
    idx = 0
    while idx < k:
        multiples_of_k_plus_idx = idx
        
        while multiples_of_k_plus_idx < len(permutation):
            if idx % 2 == 0:
                permutation[multiples_of_k_plus_idx] = bottom_v
                bottom_v += 1
            else:
                permutation[multiples_of_k_plus_idx] = top_v
                top_v -= 1
            multiples_of_k_plus_idx += k
        
        idx += 1
        
    #State: `n` is greater than 0, `k` is an even integer between 2 and `n` inclusive, `permutation` is a list of `n` values where the values at even indices are in ascending order from 1 to `n/2` and the values at odd indices are in descending order from `n` to `n/2 + 1`, `bottom_v` is `n/2 + 1`, `top_v` is `n/2`, `idx` is `k`, `multiples_of_k_plus_idx` is a multiple of `k` that is greater than or equal to `n`, stdin is empty
    result = ' '.join([str(v) for v in permutation])
    print(result)
    #This is printed: a string of space-separated numbers following the pattern of even indices in ascending order from 1 to n/2 and odd indices in descending order from n to n/2 + 1

#Overall this is what the function does:The function takes two space-separated integers n and k as input from stdin, where k is even and 2 <= k <= n <= 2 * 10^5. It generates a permutation of n values, where the values at even indices are in ascending order from 1 to n/2 and the values at odd indices are in descending order from n to n/2 + 1. The function then prints the permutation as a string of space-separated numbers.

#State of the program right berfore the function call: stdin contains one input: an integer (greater than 0).
    t = int(input())
    while t > 0:
        func_1()
        
        t -= 1
        
    #State: t is 0, stdin contains no input

#Overall this is what the function does:The function reads a positive integer from standard input and repeatedly calls another function (`func_1`) a number of times equal to the input integer, until no more input is left in standard input.

