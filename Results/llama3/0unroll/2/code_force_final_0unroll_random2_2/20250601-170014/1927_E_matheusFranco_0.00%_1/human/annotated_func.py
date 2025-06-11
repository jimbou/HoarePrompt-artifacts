#State of the program right berfore the function call: stdin contains two inputs: two space-separated integers n and k, where k is even and 2 <= k <= n <= 2 * 10^5.
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
        
    #State: Output State: idx is 0, idx_v is 1, curr_v is k+1, permutation is a list of n values where each value at index i is equal to 1 plus the smallest integer multiple of k that is greater than or equal to i, stdin is empty.
    result = ' '.join([str(v) for v in permutation])
    print(result)
    #This is printed: a string of space-separated integers, where each integer is 1 plus the smallest integer multiple of k that is greater than or equal to its index in the permutation list

#Overall this is what the function does:This function generates a permutation of n integers, where each integer is 1 plus the smallest integer multiple of k that is greater than or equal to its index in the permutation list, and prints the permutation as a string of space-separated integers.

#State of the program right berfore the function call: stdin contains one input: an integer (greater than 0).
    t = int(input())
    while t > 0:
        func_1()
        
        t -= 1
        
    #State: Output State: `t` equals 0.
    #
    #
    #
    #The output state is that the variable `t` has been decremented to 0 after the loop has executed all its iterations. The initial value of `t` was greater than 0, and with each iteration of the loop, `t` was decremented by 1 until it reached 0, at which point the loop terminated.

#Overall this is what the function does:Repeats a function call a specified number of times.

