#State of the program right berfore the function call: n and k are positive integers such that k is even and k <= n.
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
        
    #State: `n` and `k` are positive integers such that `k` is even and `k` > 0 and `k` <= `n`, `idx` is equal to `k`, `permutation` is a list of `n` integers where the elements at indices that are multiples of `k` are filled in an alternating pattern starting from 1 and `n` and the rest are zeros, `bottom_v` is `k/2` + 1 if `k` is even and `(k+1)/2` if `k` is odd, and `top_v` is `n-k/2` if `k` is even and `n-(k-1)/2` if `k` is odd, stdin contains no input.
    result = ' '.join([str(v) for v in permutation])
    print(result)
    #This is printed: a string containing the elements of the permutation list, with non-zero values at every k-th index and zeros in between, separated by spaces

#Overall this is what the function does:Generates a permutation of the numbers from 1 to n, where every k-th index is filled in an alternating pattern starting from 1 and n, and the rest are zeros, and returns it as a string with the elements separated by spaces.

#State of the program right berfore the function call: stdin contains one input: an integer (greater than 0).
    t = int(input())
    while t > 0:
        func_1()
        
        t -= 1
        
    #State: t is 0, stdin contains no input

#Overall this is what the function does:Repeats a function call a specified number of times based on user input, consuming all input from stdin, leaving no remaining input and the input counter at 0.

