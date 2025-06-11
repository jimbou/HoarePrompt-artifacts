#State of the program right berfore the function call: stdin contains one input: two space-separated integers n and k, where n and k are positive integers and k is even and k <= n.
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
        
    #State: n is a positive integer, k is a positive even integer and k <= n, permutation is a list of n zeros with all elements changed to a positive integer, idx is 0, idx_v is 1, curr_v is n + 1, stdin is empty
    result = ' '.join([str(v) for v in permutation])
    print(result)
    #This is printed: a string of n space-separated positive integers (where n is a positive integer)

#Overall this is what the function does:The function reads two positive integers n and k from standard input, where k is even and less than or equal to n. It then generates a permutation of n positive integers, where the first k elements are assigned values in ascending order, and the remaining elements are assigned values in a cyclic manner. The function prints the resulting permutation as a string of n space-separated positive integers.

#State of the program right berfore the function call: stdin contains one input: an integer (greater than 0).
    t = int(input())
    while t > 0:
        func_1()
        
        t -= 1
        
    #State: t is 0, stdin contains no input.

#Overall this is what the function does:This function reads a positive integer from standard input and executes another function (func_1) a specified number of times equal to the input integer. After execution, the input integer is decremented to 0 and standard input is left empty.

