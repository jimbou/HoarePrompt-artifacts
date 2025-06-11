#State of the program right berfore the function call: n is a positive integer and k is a positive integer such that 2 <= n <= 40 and 1 <= k <= 2n.
    cliques = ceil(n / k)
    arr = [0] * n
    cliquess = [0] * n
    for i in range(cliques):
        make_array(i * k, min((i + 1) * k - 1, n - 1), i + 1)
        
    #State: The array arr has been modified such that for each clique, the elements from i*k to min((i+1)*k-1, n-1) have been set to i+1, where i ranges from 0 to cliques-1. The values of n, k, cliques, and cliquess remain unchanged.
    print(*arr)
    #This is printed: The elements of the array arr, where each element from i*k to min((i+1)*k-1, n-1) has been set to i+1, with i ranging from 0 to cliques-1
    print(cliques)
    #This is printed: cliques (where cliques is the number of cliques)
    print(*cliquess)
    #This is printed: the elements of the list cliquess

#Overall this is what the function does:This function takes two positive integers n and k as input, where 2 <= n <= 40 and 1 <= k <= 2n. It then divides the range from 0 to n-1 into cliques of size k, and for each clique, it sets the corresponding elements in the array arr to the clique number (starting from 1). The function prints the modified array arr, the number of cliques, and the list cliquess (which remains unchanged). The function does not return any value.

#State of the program right berfore the function call: left and right are non-negative integers such that left < right, clique is a non-negative integer, arr is a list of integers of size at least right + 1, cliquess is a list of integers of size at least right + 1.
    small_element = left + 1
    big_element = right + 1
    mid = (big_element - small_element + 1) // 2
    not_mid = right - left + 1 - mid
    for i in range(mid):
        arr[left + mid - i - 1] = small_element + i
        
        cliquess[left + i] = clique
        
    #State: Output State: The values of arr from index left to left + mid - 1 are set to small_element + i, where i ranges from 0 to mid - 1. The values of cliquess from index left to left + mid - 1 are set to clique.
    for i in range(not_mid):
        arr[left + mid + i] = big_element - i
        
        cliquess[left + mid + i] = clique
        
    #State: Output State: The values of arr from index left to left + mid - 1 are set to small_element + i, where i ranges from 0 to mid - 1. The values of cliquess from index left to left + mid - 1 are set to clique. The values of arr from index left + mid to left + mid + not_mid - 1 are set to big_element - i, where i ranges from 0 to not_mid - 1. The values of cliquess from index left + mid to left + mid + not_mid - 1 are set to clique.

#Overall this is what the function does:This function modifies two lists, `arr` and `cliquess`, by assigning specific values to certain ranges of indices. It takes in parameters `left`, `right`, `clique`, `arr`, and `cliquess`. The function sets the values of `arr` from index `left` to `left + mid - 1` to `small_element + i`, where `i` ranges from 0 to `mid - 1`, and sets the corresponding values of `cliquess` to `clique`. Then, it sets the values of `arr` from index `left + mid` to `left + mid + not_mid - 1` to `big_element - i`, where `i` ranges from 0 to `not_mid - 1`, and sets the corresponding values of `cliquess` to `clique`. The function does not return any value.

