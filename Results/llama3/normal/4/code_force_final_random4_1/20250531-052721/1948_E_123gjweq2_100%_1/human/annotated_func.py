#State of the program right berfore the function call: n is a positive integer and k is a positive integer such that 2 <= n <= 40 and 1 <= k <= 2n.
    cliques = ceil(n / k)
    arr = [0] * n
    cliquess = [0] * n
    for i in range(cliques):
        make_array(i * k, min((i + 1) * k - 1, n - 1), i + 1)
        
    #State: n is a positive integer, k is a positive integer, cliques is a positive integer equal to the ceiling of n/k, arr is a list of n values where arr[i * k : min((i + 1) * k, n)] is i + 1 for i from 0 to cliques - 1, cliquess is a list of n values where cliquess[i * k : min((i + 1) * k, n)] is i + 1 for i from 0 to cliques - 1, i is cliques - 1.
    print(*arr)
    #This is printed: [cliques - 1] * k (where cliques is the ceiling of n/k and k is a positive integer)
    print(cliques)
    #This is printed: ceiling of n/k (where n is a positive integer and k is a positive integer)
    print(*cliquess)
    #This is printed: [cliques] repeated k times or the remaining elements if n is not exactly divisible by k

#Overall this is what the function does:Functionality: This function takes two positive integers, n and k, as input, where 2 <= n <= 40 and 1 <= k <= 2n. It calculates the ceiling of n/k and assigns it to the variable 'cliques'. It then initializes two lists, 'arr' and 'cliquess', of length n with all elements set to 0. The function then iterates over the range of 'cliques' and sets the values of 'arr' and 'cliquess' in a specific pattern. Finally, it prints the values of 'arr', 'cliques', and 'cliquess'. The function does not return any value.

#State of the program right berfore the function call: left and right are non-negative integers such that left < right, clique is a positive integer, arr and cliquess are lists of length at least right + 1.
    small_element = left + 1
    big_element = right + 1
    mid = (big_element - small_element + 1) // 2
    not_mid = right - left + 1 - mid
    for i in range(mid):
        arr[left + mid - i - 1] = small_element + i
        
        cliquess[left + i] = clique
        
    #State: left and right are non-negative integers such that left < right, clique is a positive integer, arr and cliquess are lists of length at least right + 1, small_element is left + 1, big_element is right + 1, mid is (right - left + 2) // 2, not_mid is right - left + 1 - mid, i is mid - 1, arr[left + mid - i - 1] is small_element + i, cliquess[left + i] is clique
    for i in range(not_mid):
        arr[left + mid + i] = big_element - i
        
        cliquess[left + mid + i] = clique
        
    #State: left and right are non-negative integers such that left < right, clique is a positive integer, arr and cliquess are lists of length at least right + 1, small_element is left + 1, big_element is right + 1, mid is (right - left + 2) // 2, not_mid is 0, i is not_mid - 1, arr[left + mid + i] is big_element - i, cliquess[left + mid + i] is clique, for all integers k such that 0 <= k < not_mid, arr[left + mid + k] is big_element - k, cliquess[left + mid + k] is clique.

#Overall this is what the function does:This function populates a portion of two lists, `arr` and `cliquess`, with values based on the input parameters `left`, `right`, and `clique`. It assigns values from `left + 1` to `right + 1` to the elements in `arr` from index `left` to `right`, and assigns the value of `clique` to the corresponding elements in `cliquess`. The function effectively creates a sequence of values in `arr` and a sequence of identical values in `cliquess`, both spanning from `left` to `right`.

