#State of the program right berfore the function call: tar is a list of positive integers, k and n are positive integers such that k <= n and n is the length of tar.
    it = 0
    ind = 0
    while ind < n and it < k:
        print(f'? {ind + 1} {tar}')
        
        x = int(input())
        
        if x == n + 1:
            return False
        
        ind = x
        
        it += 1
        
    #State: `tar` is a list of positive integers, `k` and `n` are positive integers such that `k <= n`, `n` is the length of `tar`, `it` is equal to `k`, `ind` is equal to `x`, `x` is an integer, stdin is empty, and `x` is not equal to `n + 1`, and this is printed: "? 1 [tar]" repeated `k` times.
    return ind == n and it == k
    #The program returns a boolean value indicating whether the index 'ind' is equal to the length of the list 'tar' and the iterator 'it' is equal to the positive integer 'k'.

#Overall this is what the function does:This function takes a list of positive integers `tar`, and two positive integers `k` and `n` as input, where `k` is less than or equal to `n` and `n` is the length of `tar`. It repeatedly prompts the user for input `k` times, printing a message in the format "? 1 [tar]" each time. The function then returns a boolean value indicating whether the final user input `x` is equal to the length of `tar` and the number of iterations `it` is equal to `k`. If the user inputs `n + 1` at any point, the function immediately returns `False`.

