#State of the program right berfore the function call: stdin contains t+2t lines. The first line contains one integer t (1 ≤ t ≤ 5000). Each of the next t lines contains one integer n (2 ≤ n ≤ 50). Each of the next t lines contains n space-separated integers p_1, p_2, …, p_n (1 ≤ p_i ≤ n; p_i ≠ i; all p_i are distinct).
    n = int(input())
    v = [0] * (n + 1)
    v = [0] + list(map(int, input().split()))
    for i in range(1, n + 1):
        if v[v[i]] == i:
            print(2)
            return
        
    #State: `n` is greater than or equal to 0, `i` is `n+1`, `v` is a list of `n` integers with the first element being 0, stdin contains `t+2t-2` lines. If `v[v[i]]` equals `i` for any `i` in the range 1 to `n`, the number 2 is printed. Otherwise, `v[v[i]]` is not equal to `i` for all `i` in the range 1 to `n`.
    print(3)
    #This is printed: 3

#Overall this is what the function does:This function determines whether a given list of integers represents a valid permutation or not. It accepts a list of integers as input, where each integer is a position in the list, and checks if any integer points to its own position. If such a case is found, it prints 2, indicating an invalid permutation. Otherwise, it prints 3, indicating a valid permutation. The function does not modify the input list or any other external state, and its sole purpose is to provide a validation result based on the input permutation.

