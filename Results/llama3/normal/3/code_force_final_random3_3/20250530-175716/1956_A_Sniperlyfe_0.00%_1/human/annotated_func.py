#State of the program right berfore the function call: n is a non-negative integer and p is a list of non-negative integers such that all elements in p are less than or equal to n.
    while n >= min(p):
        n -= sum(1 for x in p if x <= n)
        
    #State: n is 0 and p is a list of non-negative integers such that all elements in p are less than or equal to the original value of n.
    return n
    #The program returns 0

#Overall this is what the function does:This function takes a non-negative integer `n` and a list of non-negative integers `p` as input, where all elements in `p` are less than or equal to `n`. It repeatedly subtracts the count of elements in `p` that are less than or equal to `n` from `n` until `n` is less than the minimum value in `p`. The function returns 0, effectively reducing the input integer `n` to 0 by iteratively subtracting counts of elements from the input list `p` that are within the current value of `n`.

#State of the program right berfore the function call: n is a positive integer and p is a list of positive integers such that all elements in p are less than or equal to n and p is sorted in ascending order.
    t = int(input())
    for _ in range(t):
        k, q = map(int, input().split())
        
        p = list(map(int, input().split()))
        
        qs = list(map(int, input().split()))
        
        res = []
        
        for n in qs:
            res.append(func_1(n, p))
            print(' '.join(map(str, res)))
        
    #State: The loop has finished executing, and the list `res` contains the results of `func_1(n, p)` for all elements `n` in the list `qs`. The list `qs` is empty, and the variable `n` is the last element that was processed in the list `qs`. The list `p` remains unchanged, and the variable `t` has been decremented to 0. The variables `k` and `q` remain unchanged. The final state of the list `res` is printed, with all elements separated by spaces.

#Overall this is what the function does:The function takes a positive integer `n` and a sorted list of positive integers `p` as input, and for each element `n` in a list of query integers `qs`, it calls another function `func_1(n, p)` and appends the result to a list `res`. After processing all elements in `qs`, it prints the final state of `res` with all elements separated by spaces. The function does not modify the input list `p` or the variables `k` and `q`.

