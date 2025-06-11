#State of the program right berfore the function call: stdin contains one input: two space-separated integers n and k such that 2 <= k <= n <= 2*10^5 and k is even.
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
        
    #State: idx is equal to k, permutation is a list of length n where the first k elements are filled in an alternating pattern of increasing and decreasing values, bottom_v is equal to k/2 + 1, top_v is equal to n - k/2 + 1, and the rest of the variables remain unchanged.
    result = ' '.join([str(v) for v in permutation])
    print(result)
    #This is printed: a string of space-separated values from the permutation list, specifically the first k elements filled in an alternating pattern of increasing and decreasing values

#Overall this is what the function does:The function generates a permutation of length n, where the first k elements are filled in an alternating pattern of increasing and decreasing values, and prints the permutation as a string of space-separated values. The function takes two space-separated integers n and k as input from stdin, where 2 <= k <= n <= 2*10^5 and k is even. The function does not return any value, but instead prints the resulting permutation.

#State of the program right berfore the function call: stdin contains one input: an integer (greater than 0).
    t = int(input())
    while t > 0:
        func_1()
        
        t -= 1
        
    #State: Output State: `t` is 0, stdin contains no input.
    #
    #
    #
    #The output state after the loop executes all the iterations is that the variable `t` has been decremented to 0, and the stdin remains unchanged as it contained no input initially. The function `func_1()` has been executed `t` times, but since its effects are not specified, the output state only reflects the changes to the loop variable `t`.

#Overall this is what the function does:This function reads an integer from standard input, decrements it to 0, and executes another function (`func_1`) a number of times equal to the initial value of the integer. The function does not modify the standard input or produce any output, but it does modify the loop variable `t` to 0.

