#State of the program right berfore the function call: n is a positive integer and k is a positive integer such that 2 <= n <= 40 and 1 <= k <= 2n.
    cliques = ceil(n / k)
    arr = [0] * n
    cliquess = [0] * n
    for i in range(cliques):
        make_array(i * k, min((i + 1) * k - 1, n - 1), i + 1)
        
    #State: `n` is a positive integer such that 2 <= n <= 40, `k` is a positive integer such that 1 <= k <= 2n, `cliques` is the ceiling of n divided by k, `arr` is a list of n values where from index `i * k` to `min((i + 1) * k - 1, n - 1)` are  `i + 1` and rest are zeros, `cliquess` is a list of n values where from index `i * k` to `min((i + 1) * k - 1, n - 1)` are  `i + 1` and rest are zeros, `i` is `cliques - 1`.
    print(*arr)
    #This is printed: A list of n values where from index `i * k` to `min((i + 1) * k - 1, n - 1)` are `i + 1` and the rest are zeros, where `i` is `cliques - 1`
    print(cliques)
    #This is printed: ceiling of n divided by k (where n is a positive integer such that 2 <= n <= 40, and k is a positive integer such that 1 <= k <= 2n)
    print(*cliquess)
    #This is printed: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] (where the number of zeros is n - k and the last k elements are cliques)

#Overall this is what the function does:This function takes two positive integers n and k as input, where 2 <= n <= 40 and 1 <= k <= 2n. It calculates the ceiling of n divided by k and creates two lists of length n, arr and cliquess, where the elements from index i * k to min((i + 1) * k - 1, n - 1) are set to i + 1, and the rest are zeros. The function then prints the list arr, the calculated ceiling value, and the list cliquess. The final state of the program is that it has printed the modified list arr, the ceiling value, and the list cliquess, with the last k elements of cliquess being the ceiling value.

#State of the program right berfore the function call: left and right are non-negative integers such that left < right, clique is a positive integer, arr and cliquess are lists of length at least right + 1.
    small_element = left + 1
    big_element = right + 1
    mid = (big_element - small_element) // 2
    not_mid = right - left + 1 - mid
    for i in range(mid):
        arr[left + i] = small_element + i
        
        cliquess[left + i] = clique
        
    #State: left and right are non-negative integers such that left < right, clique is a positive integer, arr and cliquess are lists of length at least right + 1, small_element is left + 1, big_element is right + 1, mid is (right - left + 1) // 2, not_mid is right - left + 1 - mid, i is mid - 1, for all integers j in the range [0, mid), arr[left + j] is small_element + j, cliquess[left + j] is clique.
    for i in range(not_mid):
        arr[left + mid + i] = big_element - i
        
        cliquess[left + mid + i] = clique
        
    #State: left and right are non-negative integers such that left < right, clique is a positive integer, arr is a list of length at least right + 1 with arr[left + mid + i] = big_element - i, cliquess is a list of length at least right + 1 with cliquess[left + mid + i] = clique, small_element is left + 1, big_element is right + 1, mid is (right - left + 1) // 2, not_mid is 0, i is not_mid - 1

#Overall this is what the function does:The function takes in two lists, `arr` and `cliquess`, and three integers, `left`, `right`, and `clique`, as input. It then modifies the elements of `arr` and `cliquess` within the range `[left, right]` by assigning values from `left + 1` to `right + 1` in an alternating pattern, while also assigning the value of `clique` to the corresponding elements in `cliquess`. The function does not return any value.

