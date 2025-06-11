#State of the program right berfore the function call: stdin contains one input: two space-separated integers n and k, where k is even and 2 <= k <= n <= 2 * 10^5.
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
        
    #State: permutation is a list of n values where permutation[multiples_of_k_plus_i] is curr_v + n/k * (i + 1) + ((len(permutation) - 1) // k) * i, idx is 0, idx_v is 1, curr_v is curr_v + n/k * (i + 1) + ((len(permutation) - 1) // k) * i, multiples_of_k_plus_i is i + ((len(permutation) - 1) // k) * k, stdin is empty, i is k - 1, k is at least k, n is an integer between 2 * 10^5 and 2 (inclusive).
    result = ' '.join([str(v) for v in permutation])
    print(result)
    #This is printed: space-separated values of the permutation (where each value is calculated using the formula curr_v + n/k * (i + 1) + ((len(permutation) - 1) // k) * i, and i is k - 1)

#Overall this is what the function does:The function generates a permutation of n values based on the input parameters n and k, where k is even and 2 <= k <= n <= 2 * 10^5. It constructs the permutation by iterating over multiples of k plus i, where i ranges from 0 to k-1, and assigns a value to each position in the permutation based on the formula curr_v + n/k * (i + 1) + ((len(permutation) - 1) // k) * i. The function then prints the permutation as a space-separated string of values.

#State of the program right berfore the function call: stdin contains one input: an integer (greater than 0).
    t = int(input())
    while t > 0:
        func_1()
        
        t -= 1
        
    #State: t is an integer greater than or equal to 0, stdin contains no input.

#Overall this is what the function does:This function reads an integer from standard input and executes another function, func_1, a number of times equal to the input integer. After execution, the function leaves the standard input empty and the input integer is reduced to 0.

