#State of the program right berfore the function call: n and k are positive integers such that 2 <= n <= 40 and 1 <= k <= 2n.
    cliques = ceil(n / k)
    arr = [0] * n
    cliquess = [0] * n
    for i in range(cliques):
        make_array(i * k, min((i + 1) * k - 1, n - 1), i + 1)
        
    #State: `n` and `k` are positive integers such that 2 <= `n` <= 40 and 1 <= `k` <= 2`n`, `cliques` is a positive integer equal to the ceiling of `n` divided by `k`, `arr` is a list of `n` values where `arr[i * k: min((i + 1) * k, n)]` is `i + 1`, `cliquess` is a list of `n` zeros, `i` is `cliques - 1`, a value has been returned from the function `make_array(i * k, min((i + 1) * k - 1, n - 1), i + 1)` `cliques` times.
    print(*arr)
    #This is printed: 1, 1, ..., 1, 2, 2, ..., 2, ..., cliques, cliques, ..., cliques (where each value is repeated k times, and the number of segments is equal to the ceiling of n divided by k)
    print(cliques)
    #This is printed: the ceiling of n divided by k (where n is a positive integer between 2 and 40, and k is a positive integer between 1 and 2n)
    print(*cliquess)
    #This is printed: a list of n zeros (where n is a positive integer such that 2 <= n <= 40)

#Overall this is what the function does:The function takes two positive integers n and k as input, where 2 <= n <= 40 and 1 <= k <= 2n. It calculates the ceiling of n divided by k and creates a list of n values, where each segment of k values is filled with the same number, starting from 1 and incrementing for each segment. The function then prints this list, followed by the ceiling of n divided by k, and finally a list of n zeros. The function does not return any value.

#State of the program right berfore the function call: left and right are non-negative integers such that left <= right, clique is a positive integer, arr and cliquess are lists of integers with length at least right + 1.
    small_element = left + 1
    big_element = right + 1
    mid = (big_element - small_element) // 2
    not_mid = right - left + 1 - mid
    for i in range(mid):
        arr[left + i] = small_element + i
        
        cliquess[left + i] = clique
        
    #State: left and right are non-negative integers such that right is at least left, clique is a positive integer, arr and cliquess are lists of integers with length at least right + 1, arr[left + i] is equal to left + mid + i for all i from 0 to right - left, cliquess[left + i] is equal to clique for all i from 0 to right - left, small_element is left + 1, big_element is right + 1, mid is greater than or equal to 0, not_mid is right - left + 1 - (right - left + 1) // 2.
    for i in range(not_mid):
        arr[left + mid + i] = big_element - i
        
        cliquess[left + mid + i] = clique
        
    #State: left and right are non-negative integers such that right is at least left and right - left is even, clique is a positive integer, arr and cliquess are lists of integers with length at least right + 1, arr[left + i] is equal to left + mid + i for all i from 0 to right - left, cliquess[left + i] is equal to clique for all i from 0 to right - left, small_element is left + 1, big_element is right + 1, mid is greater than or equal to 0, not_mid is 0, i is not_mid, arr[left + mid + i] is big_element - i, cliquess[left + mid + i] is clique.

#Overall this is what the function does:This function modifies two lists, `arr` and `cliquess`, within a specified range defined by `left` and `right` indices. It assigns values to `arr` in a specific pattern, starting from `left + 1` and incrementing up to `right + 1`, while assigning a constant value `clique` to the corresponding indices in `cliquess`. The function effectively populates a segment of the lists with a sequence of numbers and a constant value, respectively.

