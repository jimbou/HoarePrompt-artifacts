#State of the program right berfore the function call: tar is a positive integer, k is a positive integer, n is a positive integer, 1 <= k <= n <= 10^4.
    it = 0
    ind = 0
    while ind < n and it < k:
        print(f'? {ind + 1} {tar}')
        
        x = int(input())
        
        if x == n + 1:
            return False
        
        ind = x
        
        it += 1
        
    #State: `tar` is a positive integer, `k` is a positive integer, `n` is a positive integer, `1 <= k <= n <= 10^4`, `it` is `k`, `ind` is `n`, `x` is an integer, the stdin contains no input because it has been used to get the value of `x`, and `x` is not equal to `n + 1`.
    return ind == n and it == k
    #The program returns a boolean value indicating whether `ind` is equal to `n` and `it` is equal to `k`. Since `ind` is `n` and `it` is `k`, the program returns `True`.

#Overall this is what the function does:This function takes three positive integers as input: `tar`, `k`, and `n`, where `1 <= k <= n <= 10^4`. It iteratively prompts the user for input `x` and updates the indices `ind` and `it` based on the input. The function returns `False` if the user input `x` is equal to `n + 1` at any point. Otherwise, it returns a boolean value indicating whether the final values of `ind` and `it` are equal to `n` and `k`, respectively.

