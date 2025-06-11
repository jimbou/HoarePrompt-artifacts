#State of the program right berfore the function call: tar is a positive integer, k is a positive integer, n is a positive integer such that k <= n <= 10^4.
    it = 0
    ind = 0
    while ind < n and it < k:
        print(f'? {ind + 1} {tar}')
        
        x = int(input())
        
        if x == n + 1:
            return False
        
        ind = x
        
        it += 1
        
    #State: `tar` is a positive integer, `k` is a positive integer, `n` is a positive integer such that `k <= n <= 10^4`, `it` is either `k` or the number of times the loop executed, `ind` is either `n` or the last value of `x` that was not equal to `n + 1`, `x` is an integer and is either equal to `n` or not equal to `n + 1`. Additionally, stdin contains input from the user for the number of times the loop executed.
    return ind == n and it == k
    #The program returns a boolean value indicating whether `ind` is equal to `n` and `it` is equal to `k`. `ind` is either `n` or the last value of `x` that was not equal to `n + 1`, and `it` is either `k` or the number of times the loop executed, which is provided by the user through stdin. The boolean value returned is based on the conditions that `ind` equals `n` and `it` equals `k`, where `n` and `k` are positive integers and `k` is less than or equal to `n`, which is less than or equal to 10^4.

#Overall this is what the function does:This function takes three positive integers as input: `tar`, `k`, and `n`, where `k` is less than or equal to `n` and `n` is less than or equal to 10^4. It then enters a loop that continues until either `n` iterations have been reached or `k` iterations have been executed. In each iteration, the function prints a query to the user and reads an integer input from the user. If the input is equal to `n + 1`, the function immediately returns `False`. Otherwise, the function updates its internal state based on the user's input. After the loop, the function returns a boolean value indicating whether the number of iterations executed (`it`) is equal to `k` and the last input value (`ind`) is equal to `n`.

