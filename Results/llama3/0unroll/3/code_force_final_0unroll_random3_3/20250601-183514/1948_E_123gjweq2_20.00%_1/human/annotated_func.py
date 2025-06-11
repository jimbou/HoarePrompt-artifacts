#State of the program right berfore the function call: n is a positive integer and k is a positive integer such that 2 <= n <= 40 and 1 <= k <= 2n.
    cliques = ceil(n / k)
    arr = [0] * n
    cliquess = [0] * n
    for i in range(cliques):
        make_array(i * k, min((i + 1) * k - 1, n - 1), i + 1)
        
    #State: arr is a list of n integers, where the first k elements are 1, the next k elements are 2, and so on, until the last k elements are cliques, and cliquess is a list of n integers, where the first k elements are 1, the next k elements are 2, and so on, until the last k elements are cliques.
    print(*arr)
    #This is printed: a sequence of k repetitions of each integer from 1 to cliques
    print(cliques)
    #This is printed: A list of n integers, where the first k elements are 1, the next k elements are 2, and so on, until the last k elements are [cliques] (where [cliques] is the value of the last set of k elements)
    print(*cliquess)
    #This is printed: 1 (k times), 2 (k times), 3 (k times), ..., cliques (k times)

#Overall this is what the function does:The function generates two lists, `arr` and `cliquess`, each containing a sequence of integers. The sequence consists of `k` repetitions of each integer from 1 to `cliques`, where `cliques` is the ceiling of `n` divided by `k`. The function then prints the contents of `arr`, the value of `cliques`, and the contents of `cliquess`. The final state of the program is that these printed values are displayed, with no modifications made to the input variables `n` and `k`.

#State of the program right berfore the function call: left and right are non-negative integers such that left < right, clique is a positive integer, arr and cliquess are lists of length at least right + 1.
    small_element = left + 1
    big_element = right + 1
    mid = (big_element - small_element) // 2
    not_mid = right - left + 1 - mid
    for i in range(mid):
        arr[left + i] = small_element + i
        
        cliquess[left + i] = clique
        
    #State: Output State: left and right are non-negative integers such that left < right, clique is a positive integer, arr and cliquess are lists of length at least right + 1, small_element is left + 1, big_element is right + 1, mid is (right - left + 1) // 2, not_mid is right - left + 1 - ((right - left + 1) // 2), arr[left: left + mid] is a list of consecutive integers from small_element to small_element + mid - 1, and cliquess[left: left + mid] is a list of clique repeated mid times.
    for i in range(not_mid):
        arr[left + mid + i] = big_element - i
        
        cliquess[left + mid + i] = clique
        
    #State: Output State: left and right are non-negative integers such that left < right, clique is a positive integer, arr and cliquess are lists of length at least right + 1, small_element is left + 1, big_element is right + 1, mid is (right - left + 1) // 2, not_mid is right - left + 1 - ((right - left + 1) // 2), arr[left: left + mid] is a list of consecutive integers from small_element to small_element + mid - 1, cliquess[left: left + mid] is a list of clique repeated mid times, and arr[left + mid: right + 1] is a list of consecutive integers from big_element - not_mid + 1 to big_element, and cliquess[left + mid: right + 1] is a list of clique repeated not_mid times.

#Overall this is what the function does:This function modifies two lists, `arr` and `cliquess`, by assigning consecutive integers and a repeated clique value to specific ranges within these lists. It takes in parameters `left`, `right`, and `clique`, where `left` and `right` are non-negative integers with `left < right`, and `clique` is a positive integer. The function divides the range from `left` to `right` into two parts, assigning smaller consecutive integers to the first part and larger consecutive integers to the second part of the range in `arr`, while assigning the `clique` value to corresponding parts in `cliquess`. The function returns no value but modifies the input lists `arr` and `cliquess` in place.

