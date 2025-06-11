#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 5000) followed by t test cases. Each test case consists of an integer n (2 <= n <= 50) followed by n distinct integers p_i (1 <= p_i <= n; p_i != i).
    n = int(input())
    v = [0] * (n + 1)
    v = [0] + list(map(int, input().split()))
    for i in range(1, n + 1):
        if v[v[i]] == i:
            print(2)
            return
        
    #State: `n` is at least 2, `i` is `n`, `v` is a list of `n+1` integers where the first element is 0 and the remaining elements are distinct integers between 1 and `n` inclusive, stdin contains `t-1` test cases. If the value at index `v[i]` in the list `v` equals `i` at any point during the loop, then the number 2 is printed and the loop terminates early. Otherwise, the loop completes all iterations without printing anything.
    print(3)
    #This is printed: 3

#Overall this is what the function does:This function reads an integer n and a list of n distinct integers from standard input, then checks if any integer in the list is equal to its index in the list (1-indexed). If a match is found, it prints 2 and returns; otherwise, it prints 3. The function does not modify the input values or store any results, and it does not handle cases where the input is invalid or malformed.

