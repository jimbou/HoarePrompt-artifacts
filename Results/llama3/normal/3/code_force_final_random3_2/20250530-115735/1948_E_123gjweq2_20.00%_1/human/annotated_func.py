#State of the program right berfore the function call: n is a positive integer and k is a positive integer such that 2 <= n <= 40 and 1 <= k <= 2n.
    cliques = ceil(n / k)
    arr = [0] * n
    cliquess = [0] * n
    for i in range(cliques):
        make_array(i * k, min((i + 1) * k - 1, n - 1), i + 1)
        
    #State: `n` is a positive integer such that 2 <= n <= 40, `k` is a positive integer such that 1 <= k <= 2n, `cliques` is a positive integer, `arr` is a list of n integers where the first `cliques * k` elements are `cliques`, `cliquess` is a list of n zeros, `i` is `cliques - 1`, and a value has been returned from the function `make_array` with arguments `(cliques - 1) * k`, `min(cliques * k - 1, n - 1)`, and `cliques`.
    print(*arr)
    #This is printed: [cliques] * (cliques * k) + [unknown elements]
    print(cliques)
    #This is printed: cliques (where cliques is a positive integer)
    print(*cliquess)
    #This is printed: 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 (where n is the number of zeros in the list cliquess)

#Overall this is what the function does:The function takes two positive integers n and k as input, where 2 <= n <= 40 and 1 <= k <= 2n. It calculates the ceiling of n/k and assigns it to the variable cliques. It then initializes two lists, arr and cliquess, of length n with all elements set to 0. The function then iterates over the range of cliques, calling the function make_array with arguments i*k, min((i+1)*k-1, n-1), and i+1. After the loop, the function prints the list arr, which contains the value cliques repeated cliques*k times followed by unknown elements. It then prints the value of cliques and finally prints the list cliquess, which contains all zeros. The function does not return any value.

#State of the program right berfore the function call: left and right are non-negative integers such that left < right, clique is a non-negative integer, arr and cliquess are lists of non-negative integers with length at least right + 1.
    small_element = left + 1
    big_element = right + 1
    mid = (big_element - small_element) // 2
    not_mid = right - left + 1 - mid
    for i in range(mid):
        arr[left + i] = small_element + i
        
        cliquess[left + i] = clique
        
    #State: left and right are non-negative integers such that right - left + 1 is at least 2, clique is a non-negative integer, arr is a list of non-negative integers with length at least right + 1 where arr[left] is small_element, arr[left + 1] is small_element + 1, ..., arr[left + mid - 1] is small_element + mid - 1, cliquess is a list of non-negative integers with length at least right + 1 where cliquess[left] is clique, cliquess[left + 1] is clique, ..., cliquess[left + mid - 1] is clique, small_element is left + 1, big_element is right + 1, mid is (right - left + 1) // 2, not_mid is right - left + 1 - ((right - left + 1) // 2), i is mid
    for i in range(not_mid):
        arr[left + mid + i] = big_element - i
        
        cliquess[left + mid + i] = clique
        
    #State: left and right are non-negative integers such that right - left + 1 is at least 2, clique is a non-negative integer, arr is a list of non-negative integers with length at least right + 1 where arr[left] is small_element, arr[left + 1] is small_element + 1, ..., arr[left + mid - 1] is small_element + mid - 1, arr[left + mid] is big_element, arr[left + mid + 1] is big_element - 1, ..., arr[left + mid + not_mid - 1] is big_element - not_mid + 1, cliquess is a list of non-negative integers with length at least right + 1 where cliquess[left] is clique, cliquess[left + 1] is clique, ..., cliquess[left + mid - 1] is clique, cliquess[left + mid] is clique, cliquess[left + mid + 1] is clique, ..., cliquess[left + mid + not_mid - 1] is clique, small_element is left + 1, big_element is right + 1, mid is (right - left + 1) // 2, not_mid is 0, i is not_mid.

#Overall this is what the function does:The function modifies two lists, `arr` and `cliquess`, by assigning values to a subset of their elements. It takes a range defined by `left` and `right` indices and a `clique` value as input. The function first calculates the midpoint of the range and then assigns incrementing values starting from `left + 1` to the first half of the range in `arr`, and the value of `clique` to the corresponding indices in `cliquess`. It then assigns decrementing values starting from `right + 1` to the second half of the range in `arr`, and the value of `clique` to the corresponding indices in `cliquess`. The function does not return any value, but modifies the input lists in place.

