#State of the program right berfore the function call: n is a positive integer and k is a positive integer such that 2 <= n <= 40 and 1 <= k <= 2n.
    cliques = ceil(n / k)
    arr = [0] * n
    cliquess = [0] * n
    for i in range(cliques):
        make_array(i * k, min((i + 1) * k - 1, n - 1), i + 1)
        
    #State: `n` is a positive integer, `k` is a positive integer, `cliques` is a positive integer, `arr` is a list of n integers where the integers from index `i * k` to `min((i + 1) * k - 1, n - 1)` are equal to `i + 1`, `cliquess` is a list of n zeros, `i` is `cliques - 1`, `make_array` function is called with arguments `i * k`, `min((i + 1) * k - 1, n - 1)`, and `i + 1`.
    print(*arr)
    #This is printed: [1, 1, ..., 2, 2, ..., 3, 3, ..., ..., cliques, cliques, ..., cliques] (where the number of times each integer appears is k, and the last integer is repeated until the end of the list)
    print(cliques)
    #This is printed: cliques (where cliques is a positive integer)
    print(*cliquess)
    #This is printed: 0 0 0 ... 0 (where there are n zeros)

#Overall this is what the function does:The function takes two positive integers `n` and `k` as input, where `2 <= n <= 40` and `1 <= k <= 2n`. It then creates a list `arr` of `n` integers, where each integer from `i * k` to `min((i + 1) * k - 1, n - 1)` is set to `i + 1`, effectively dividing the list into segments of size `k` and assigning a unique integer to each segment. The function then prints the modified list `arr`, the number of segments `cliques`, and a list of `n` zeros `cliquess`.

#State of the program right berfore the function call: left and right are non-negative integers such that left < right, arr is a list of non-negative integers of length at least right + 1, cliquess is a list of non-negative integers of length at least right + 1, and clique is a non-negative integer.
    small_element = left + 1
    big_element = right + 1
    mid = (big_element - small_element + 1) // 2
    not_mid = right - left + 1 - mid
    for i in range(mid):
        arr[left + mid - i - 1] = small_element + i
        
        cliquess[left + i] = clique
        
    #State: left and right are non-negative integers such that left < right, arr is a list of non-negative integers of length at least right + 1, cliquess is a list of non-negative integers of length at least right + 1, clique is a non-negative integer, small_element is left + 1, big_element is right + 1, mid is greater than or equal to 0, not_mid is right - left + 1 - mid, i is mid, arr[left + mid - i - 1] is small_element + i, cliquess[left + i] is clique
    for i in range(not_mid):
        arr[left + mid + i] = big_element - i
        
        cliquess[left + mid + i] = clique
        
    #State: left and right are non-negative integers such that left < right, arr is a list of non-negative integers of length at least right + 1, cliquess is a list of non-negative integers of length at least right + 1, clique is a non-negative integer, small_element is left + 1, big_element is right + 1, mid is greater than or equal to 0, not_mid is greater than or equal to 0, i is mid + not_mid, arr[left + mid - i - 1] is small_element + i, cliquess[left + i] is clique, arr[left + mid + i] is big_element - i, cliquess[left + mid + i] is clique

#Overall this is what the function does:The function assigns values to a subset of a list 'arr' and another list 'cliquess' within a specified range. It takes in parameters 'left', 'right', 'arr', 'cliquess', and 'clique'. The function first calculates the midpoint 'mid' of the range from 'left' to 'right' and then assigns values to the elements in 'arr' and 'cliquess' in two parts: the first part assigns values from 'left + 1' to 'left + mid' in descending order, and the second part assigns values from 'left + mid' to 'right' in ascending order. The values assigned to 'cliquess' are all set to 'clique'. The function modifies the input lists 'arr' and 'cliquess' in place and does not return any value.

