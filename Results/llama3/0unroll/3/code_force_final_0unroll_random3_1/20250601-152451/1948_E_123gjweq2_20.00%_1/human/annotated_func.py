#State of the program right berfore the function call: n is a positive integer and k is a positive integer such that 2 <= n <= 40 and 1 <= k <= 2n.
    cliques = ceil(n / k)
    arr = [0] * n
    cliquess = [0] * n
    for i in range(cliques):
        make_array(i * k, min((i + 1) * k - 1, n - 1), i + 1)
        
    #State: The output state is a positive integer n and a positive integer k such that 2 <= n <= 40 and 1 <= k <= 2n, cliques is an integer equal to the ceiling of n divided by k, arr is a list of n integers where each integer from index i * k to min((i + 1) * k - 1, n - 1) is equal to i + 1, cliquess is a list of n zeros.
    print(*arr)
    #This is printed: A sequence of integers, where each integer is repeated k times, and the value of each integer is the chunk index plus one.
    print(cliques)
    #This is printed: ceiling of n divided by k (where n and k are the given positive integers)
    print(*cliquess)
    #This is printed: A list of n zeros

#Overall this is what the function does:This function takes two positive integers n and k as input, where 2 <= n <= 40 and 1 <= k <= 2n. It then divides the range of n into chunks of size k, assigns a unique integer to each chunk (starting from 1), and repeats this integer k times in the chunk. The function prints the resulting sequence of integers, the number of chunks (ceiling of n divided by k), and a list of n zeros. The function does not return any values, but rather prints the results directly.

#State of the program right berfore the function call: left and right are non-negative integers such that left < right, and clique is a positive integer. The array arr and cliquess are lists of length at least right + 1, and arr is initially empty.
    small_element = left + 1
    big_element = right + 1
    mid = (big_element - small_element) // 2
    not_mid = right - left + 1 - mid
    for i in range(mid):
        arr[left + i] = small_element + i
        
        cliquess[left + i] = clique
        
    #State: left and right are non-negative integers such that left < right, clique is a positive integer, arr is a list of length at least right + 1 with elements from index left to left + mid - 1 set to small_element + i where i is the index, cliques is a list of length at least right + 1 with elements from index left to left + mid - 1 set to clique, small_element is left + 1, big_element is right + 1, mid is (right - left + 1) // 2, and not_mid is right - left + 1 - mid.
    for i in range(not_mid):
        arr[left + mid + i] = big_element - i
        
        cliquess[left + mid + i] = clique
        
    #State: Output State: The elements of arr from index left to left + mid - 1 are set to small_element + i where i is the index, and the elements of arr from index left + mid to right are set to big_element - i where i is the index. The elements of cliques from index left to left + mid - 1 are set to clique, and the elements of cliques from index left + mid to right are set to clique.

#Overall this is what the function does:The function populates a specified range in two lists, `arr` and `cliques`, with values based on the input parameters `left`, `right`, and `clique`. It sets the elements in the first half of the range in `arr` to incrementing values starting from `left + 1`, and the elements in the second half to decrementing values starting from `right + 1`. The corresponding elements in `cliques` are set to the value of `clique`. The function modifies the input lists `arr` and `cliques` in place, and does not return any value.

