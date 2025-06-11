#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 5000) followed by t test cases. Each test case consists of an integer n (2 <= n <= 50) followed by n distinct integers p_1, p_2, ..., p_n (1 <= p_i <= n; p_i != i).
    n = int(input())
    v = [0] * (n + 1)
    v = [0] + list(map(int, input().split()))
    for i in range(1, n + 1):
        if v[v[i]] == i:
            print(2)
            return
        
    #State: `n` is at least `n`, `i` is `n+1`, `v` is a list of `n+1` integers where the first element is 0 and the remaining elements are the `n` distinct integers `p_1, p_2, ..., p_n` (1 <= `p_i` <= `n`; `p_i` != `i`), stdin contains `t-n` test cases. If the value at index `v[i]` in list `v` is equal to `i` at any point during the loop execution, then the number 2 is printed. Otherwise, no action is taken.
    print(3)
    #This is printed: 3

#Overall this is what the function does:This function reads an integer n and a list of n distinct integers from standard input, then checks if any integer in the list is equal to its 1-based index. If a match is found, it prints 2; otherwise, it prints 3. The function does not modify the input values or perform any other actions beyond printing a single integer.

