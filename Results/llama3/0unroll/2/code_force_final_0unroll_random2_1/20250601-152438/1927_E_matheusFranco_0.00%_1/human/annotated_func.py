#State of the program right berfore the function call: stdin contains two inputs: two integers n and k, where k is even and 2 <= k <= n <= 2 * 10^5.
    n, k = map(int, input().split(' '))
    permutation = [0] * n
    idx = 0
    idx_v = 1
    curr_v = 1
    for i in range(k):
        multiples_of_k_plus_i = i
        
        while multiples_of_k_plus_i < len(permutation):
            permutation[multiples_of_k_plus_i] = curr_v
            curr_v += 1
            multiples_of_k_plus_i += k
        
    #State: Output State: The list permutation contains k non-zero values, and the variable curr_v is equal to k+1. The values of n, k, idx, idx_v, and stdin remain unchanged.
    result = ' '.join([str(v) for v in permutation])
    print(result)
    #This is printed: a string containing k non-zero values separated by spaces (where k is a fixed value)

#Overall this is what the function does:This function generates a permutation of length n, where the first k non-zero values are assigned in a specific pattern, and prints the resulting permutation as a string of space-separated values. The function takes two integers n and k as input from stdin, where k is even and 2 <= k <= n <= 2 * 10^5, and leaves the input variables unchanged. The output string contains k non-zero values separated by spaces.

#State of the program right berfore the function call: stdin contains one input: an integer (greater than 0).
    t = int(input())
    while t > 0:
        func_1()
        
        t -= 1
        
    #State: Output State: `t` is 0, stdin contains no input.
    #
    #
    #
    #The output state is that the variable `t` has been decremented to 0, and the stdin remains unchanged as it was not affected by the loop. The function `func_1()` was executed `t` times, but since its effects are not specified, we cannot determine any further changes to the state.

#Overall this is what the function does:Reads an integer from standard input, decrements it to 0, and executes another function (`func_1`) a number of times equal to the initial integer value, without modifying the standard input.

