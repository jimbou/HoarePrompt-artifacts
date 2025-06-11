#State of the program right berfore the function call: n is a positive integer and k is a positive integer such that 2 <= n <= 40 and 1 <= k <= 2n.
    cliques = ceil(n / k)
    arr = [0] * n
    cliquess = [0] * n
    for i in range(cliques):
        make_array(i * k, min((i + 1) * k - 1, n - 1), i + 1)
        
    #State: n is a positive integer such that 2 <= n <= 40, k is a positive integer such that 1 <= k <= 2n, cliques is an integer equal to the ceiling of n/k, arr is a list of n integers where arr[i * k : min((i + 1) * k, n)] is equal to i + 1, cliquess is a list of n zeros, i is equal to cliques - 1, the value of make_array(i * k, min((i + 1) * k - 1, n - 1), i + 1) has been returned cliques times.
    print(*arr)
    #This is printed: A sequence of integers where each integer from 1 to cliques is repeated k times, and the value of cliques is the ceiling of n/k
    print(cliques)
    #This is printed: ceiling of n/k (where n is a positive integer between 2 and 40, and k is a positive integer between 1 and 2n)
    print(*cliquess)
    #This is printed: 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 (where n is the number of zeros and n is a positive integer such that 2 <= n <= 40)

#Overall this is what the function does:The function takes two positive integers n and k as input, where 2 <= n <= 40 and 1 <= k <= 2n. It calculates the ceiling of n/k and creates a list of n integers, where each integer from 1 to the ceiling value is repeated k times. The function then prints this list, the ceiling value, and a list of n zeros. The function does not return any value, but rather prints the results directly.

#State of the program right berfore the function call: left and right are non-negative integers such that left < right, clique is a non-negative integer, arr is a list of integers of length at least right + 1, and cliquess is a list of integers of length at least right + 1.
    small_element = left + 1
    big_element = right + 1
    mid = (big_element - small_element + 1) // 2
    not_mid = right - left + 1 - mid
    for i in range(mid):
        arr[left + mid - i - 1] = small_element + i
        
        cliquess[left + i] = clique
        
    #State: left and right are non-negative integers such that left < right, clique is a non-negative integer, arr is a list of integers of length at least right + 1 where arr[left + mid - i - 1] is small_element + i for all i in range(mid), cliquess is a list of integers of length at least right + 1 where cliquess[left + i] is clique for all i in range(mid), small_element is left + 1, big_element is right + 1, mid is greater than or equal to 0, not_mid is right - left + 1 - mid, and i is mid - 1.
    for i in range(not_mid):
        arr[left + mid + i] = big_element - i
        
        cliquess[left + mid + i] = clique
        
    #State: left and right are non-negative integers such that left < right, clique is a non-negative integer, arr is a list of integers of length at least right + 1 where arr[left + mid - i - 1] is small_element + i for all i in range(mid), and arr[left + mid + i] is big_element - i for all i in range(not_mid), cliquess is a list of integers of length at least right + 1 where cliquess[left + i] is clique for all i in range(mid), and cliquess[left + mid + i] is clique for all i in range(not_mid), small_element is left + 1, big_element is right + 1, mid is greater than or equal to 0, not_mid is greater than or equal to 0, and i is not_mid - 1.

#Overall this is what the function does:The function takes in a list of integers `arr` and a list of integers `cliquess`, along with three integers `left`, `right`, and `clique`. It modifies the elements of `arr` and `cliquess` within the range `left` to `right` (inclusive) in a specific pattern. The function first sets the elements of `arr` from `left` to `left + mid - 1` to a sequence of increasing integers starting from `left + 1`, and sets the corresponding elements of `cliquess` to `clique`. Then, it sets the elements of `arr` from `left + mid` to `right` to a sequence of decreasing integers starting from `right + 1`, and sets the corresponding elements of `cliquess` to `clique`. The function does not return any value.

