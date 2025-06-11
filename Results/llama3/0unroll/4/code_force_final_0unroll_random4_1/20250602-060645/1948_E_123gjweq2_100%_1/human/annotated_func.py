#State of the program right berfore the function call: n is a positive integer and k is a positive integer such that 2 <= n <= 40 and 1 <= k <= 2n.
    cliques = ceil(n / k)
    arr = [0] * n
    cliquess = [0] * n
    for i in range(cliques):
        make_array(i * k, min((i + 1) * k - 1, n - 1), i + 1)
        
    #State: arr is a list of n values where each value at index j is equal to the ceiling of (j/k) + 1, cliquess is a list of n values where each value at index j is equal to the ceiling of (j/k) + 1, n is a positive integer and k is a positive integer such that 2 <= n <= 40 and 1 <= k <= 2n, cliques is the ceiling of n/k.
    print(*arr)
    #This is printed: the ceiling of (0/k) + 1, the ceiling of (1/k) + 1, the ceiling of (2/k) + 1, ..., the ceiling of ((n-1)/k) + 1 (where n is a positive integer and k is a positive integer such that 2 <= n <= 40 and 1 <= k <= 2n)
    print(cliques)
    #This is printed: ceiling of n/k (where n is a positive integer and k is a positive integer such that 2 <= n <= 40 and 1 <= k <= 2n)
    print(*cliquess)
    #This is printed: 1, 2, 3, ..., ceiling of n/k (where ceiling of n/k is the ceiling of n/k)

#Overall this is what the function does:This function takes two positive integers n and k as input, where 2 <= n <= 40 and 1 <= k <= 2n. It calculates the ceiling of n/k and uses this value to create three lists: arr, cliquess, and a variable cliques. The function then prints the values in arr, the value of cliques, and the values in cliquess. The values in arr and cliquess are the ceiling of (j/k) + 1 for each index j, and the value of cliques is the ceiling of n/k. The function does not return any values, but rather prints the calculated values.

#State of the program right berfore the function call: left and right are non-negative integers such that left <= right, clique is a positive integer, arr is a list of length at least right + 1, and cliquess is a list of length at least right + 1.
    small_element = left + 1
    big_element = right + 1
    mid = (big_element - small_element + 1) // 2
    not_mid = right - left + 1 - mid
    for i in range(mid):
        arr[left + mid - i - 1] = small_element + i
        
        cliquess[left + i] = clique
        
    #State: Output State: The elements of arr from index left to left + mid - 1 are filled with values from small_element to small_element + mid - 1 in reverse order, and the elements of cliquess from index left to left + mid - 1 are filled with the value of clique.
    for i in range(not_mid):
        arr[left + mid + i] = big_element - i
        
        cliquess[left + mid + i] = clique
        
    #State: Output State: The elements of arr from index left + mid to left + mid + not_mid - 1 are filled with values from big_element - not_mid + 1 to big_element in reverse order, and the elements of cliquess from index left + mid to left + mid + not_mid - 1 are filled with the value of clique.

#Overall this is what the function does:This function fills two lists, `arr` and `cliquess`, with values in a specific pattern. It takes in parameters `left`, `right`, `clique`, `arr`, and `cliquess`. The function first calculates the midpoint of the range `left` to `right` and then fills the first half of the range in `arr` with values from `small_element` to `small_element + mid - 1` in reverse order, and the corresponding elements in `cliquess` with the value of `clique`. Then, it fills the second half of the range in `arr` with values from `big_element - not_mid + 1` to `big_element` in reverse order, and the corresponding elements in `cliquess` with the value of `clique`. The function modifies the input lists `arr` and `cliquess` in place.

