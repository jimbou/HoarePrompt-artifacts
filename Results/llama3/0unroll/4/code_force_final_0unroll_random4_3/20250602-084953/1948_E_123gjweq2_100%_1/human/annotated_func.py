#State of the program right berfore the function call: n and k are positive integers such that 2 <= n <= 40 and 1 <= k <= 2n.
    cliques = ceil(n / k)
    arr = [0] * n
    cliquess = [0] * n
    for i in range(cliques):
        make_array(i * k, min((i + 1) * k - 1, n - 1), i + 1)
        
    #State: arr is a list of n integers where the value at each index is equal to the ceiling of the index divided by k plus 1, cliquess is a list of n integers where the value at each index is equal to the ceiling of the index divided by k plus 1.
    print(*arr)
    #This is printed: [ceiling(index/k) + 1 for index in range(n)]
    print(cliques)
    #This is printed: a list of n integers where the value at each index is equal to the ceiling of the index divided by k plus 1
    print(*cliquess)
    #This is printed: the elements of the list cliquess (where each element is the ceiling of the index divided by k plus 1)

#Overall this is what the function does:This function generates two lists, `arr` and `cliquess`, each containing `n` integers, where the value at each index is equal to the ceiling of the index divided by `k` plus 1. It then prints these lists, as well as the number of cliques (`cliques`). The function takes two positive integers `n` and `k` as input, where `2 <= n <= 40` and `1 <= k <= 2n`. The function does not return any values, but rather prints the results directly.

#State of the program right berfore the function call: left and right are non-negative integers such that left < right, clique is a non-negative integer, arr and cliquess are lists of non-negative integers with length at least right + 1.
    small_element = left + 1
    big_element = right + 1
    mid = (big_element - small_element + 1) // 2
    not_mid = right - left + 1 - mid
    for i in range(mid):
        arr[left + mid - i - 1] = small_element + i
        
        cliquess[left + i] = clique
        
    #State: Output State: The elements of the list arr from index left + mid - 1 to left - 1 are filled with consecutive integers from small_element to small_element + mid - 1. The elements of the list cliquess from index left to left + mid - 1 are filled with the value of clique.
    for i in range(not_mid):
        arr[left + mid + i] = big_element - i
        
        cliquess[left + mid + i] = clique
        
    #State: Output State: The elements of the list arr from index left + mid - 1 to left - 1 are filled with consecutive integers from small_element to small_element + mid - 1. The elements of the list cliquess from index left to left + mid - 1 are filled with the value of clique. The elements of the list arr from index left + mid to left + mid + not_mid - 1 are filled with consecutive integers from big_element - not_mid + 1 to big_element. The elements of the list cliquess from index left + mid to left + mid + not_mid - 1 are filled with the value of clique.

#Overall this is what the function does:The function fills two lists, arr and cliquess, with specific values within a specified range. It takes in parameters left, right, clique, arr, and cliquess. The function first calculates mid and not_mid values based on the left and right parameters. It then fills the arr list with consecutive integers from small_element to small_element + mid - 1 and from big_element - not_mid + 1 to big_element, while filling the corresponding cliquess list with the value of clique. The function modifies the input lists arr and cliquess in place, without returning any values.

