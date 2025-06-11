#State of the program right berfore the function call: n is a positive integer and k is a positive integer such that 2 <= n <= 40 and 1 <= k <= 2n.
    cliques = ceil(n / k)
    arr = [0] * n
    cliquess = [0] * n
    for i in range(cliques):
        make_array(i * k, min((i + 1) * k - 1, n - 1), i + 1)
        
    #State: n is a positive integer, k is a positive integer, cliques is a positive integer, arr is a list of n integers where each integer is equal to the number of the clique it belongs to, cliquess is a list of n integers where each integer is equal to the number of the clique it belongs to.
    print(*arr)
    #This is printed: [clique number 1], [clique number 2], ..., [clique number n] (where each clique number is an integer representing the clique that the corresponding element in the list belongs to)
    print(cliques)
    #This is printed: the number of cliques
    print(*cliquess)
    #This is printed: [clique numbers for each element in the list cliquess]

#Overall this is what the function does:This function takes two positive integers n and k as input, where 2 <= n <= 40 and 1 <= k <= 2n. It divides the range of n into cliques of size k, assigns each element in the range to a clique, and prints the clique number for each element. The function also prints the total number of cliques and the clique numbers for each element in a separate list. The output provides a mapping of each element in the range to its corresponding clique number, effectively partitioning the range into cliques of size k.

#State of the program right berfore the function call: left and right are non-negative integers such that left < right, clique is a positive integer, arr and cliquess are lists of length at least right + 1.
    small_element = left + 1
    big_element = right + 1
    mid = (big_element - small_element) // 2
    not_mid = right - left + 1 - mid
    for i in range(mid):
        arr[left + i] = small_element + i
        
        cliquess[left + i] = clique
        
    #State: Output State: The elements of arr from index left to left + mid - 1 are populated with consecutive integers starting from small_element, and the corresponding elements in cliquess are set to clique.
    for i in range(not_mid):
        arr[left + mid + i] = big_element - i
        
        cliquess[left + mid + i] = clique
        
    #State: Output State: The elements of arr from index left + mid to left + mid + not_mid - 1 are populated with consecutive integers starting from big_element - not_mid + 1 and ending at big_element, and the corresponding elements in cliquess are set to clique.

#Overall this is what the function does:Populates a portion of two lists, `arr` and `cliquess`, with specific values. It takes a range defined by `left` and `right`, and a `clique` value as input. The function sets consecutive integers in `arr` starting from `small_element` (left + 1) up to `big_element` (right + 1), divided into two segments at the midpoint, and assigns the `clique` value to the corresponding elements in `cliquess`. The function modifies the input lists in place, without returning any value.

