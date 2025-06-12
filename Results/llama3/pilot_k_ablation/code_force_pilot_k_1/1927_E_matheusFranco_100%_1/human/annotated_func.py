#State of the program right berfore the function call: stdin contains one input: two space-separated integers n and k, where k is even and 2 <= k <= n <= 2 * 10^5.
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
        
    #State: `permutation` is an array of `n` values where every `k`th index is filled with a value, `idx` is equal to `k`, `n` is an integer between 2 and 2 * 10^5 inclusive, `k` is an even integer between 2 and `n` inclusive, `stdin` is empty, `bottom_v` is equal to `n/2` plus 1 if `n` is even and `n/2` plus 1 if `n` is odd, `top_v` is equal to `n/2` if `n` is even and `n/2` if `n` is odd, `multiples_of_k_plus_idx` is equal to `n`
    result = ' '.join([str(v) for v in permutation])
    print(result)
    #This is printed: the elements of the permutation array separated by spaces

#Overall this is what the function does:This function reads two space-separated integers n and k from standard input, where k is even and 2 <= k <= n <= 2 * 10^5, and generates a permutation of n values. It fills every kth index of the permutation with a value, alternating between incrementing from 1 and decrementing from n, and prints the permutation as a string of space-separated values. The function does not return any value, but rather prints the result directly.

#State of the program right berfore the function call: stdin contains one input: an integer (greater than 0).
    t = int(input())
    while t > 0:
        func_1()
        
        t -= 1
        
    #State: t is 0, func_1() has been executed t times where t is the initial value of t

#Overall this is what the function does:Executes the function func_1() a specified number of times, as determined by the initial value of the input integer t, until t reaches 0.

