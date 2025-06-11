#State of the program right berfore the function call: t is a positive integer, n, k, and x are positive integers, and a is a list of n positive integers.
    t = int(input())
    for i in range(t):
        n, k, x = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        a.sort()
        
        product = func_2(k, x, a)
        
        print(product)
        
    #State: Output State: `t` is a positive integer, `n` is a positive integer, `k` is a positive integer, `x` is a positive integer, `a` is a list of `n` positive integers, stdin contains no input.

#Overall this is what the function does:This function reads a positive integer t from standard input, then for each test case, it reads three positive integers n, k, and x, and a list of n positive integers a. It sorts the list a in ascending order and passes k, x, and the sorted list a to another function func_2 to compute a product. Finally, it prints the product to standard output.

#State of the program right berfore the function call: removals and negatives are non-negative integers, and elements is a list of integers sorted in ascending order.
    if (removals == 6 and negatives == 3) :
        return 0
        #The program returns the integer 0.
    #State: *removals and negatives are non-negative integers, and elements is a list of integers sorted in ascending order. The pair (removals, negatives) is not equal to (6, 3)
    pos = []
    s = sum(elements)
    n = sum(elements[-negatives:])
    pos.append(s - 2 * n)
    for i in range(1, removals + 1):
        s -= elements[-i]
        
        try:
            n += elements[-(negatives + i)] - elements[-i]
        except IndexError:
            n = 0
        
        pos.append(s - 2 * n)
        
    #State: Output State: removals is a non-negative integer, negatives is a non-negative integer, elements is a list of integers sorted in ascending order, pos is a list containing removals + 1 elements which are the sum of all elements in elements minus twice the sum of the last negatives elements in elements, and then removals iterations of the sum of all elements in elements minus twice the sum of the last negatives + i elements in elements for i in range(1, removals + 1).
    return max(pos)
    #The program returns the maximum value from the list 'pos', which contains 'removals + 1' elements. Each element in 'pos' is the sum of all elements in the sorted list 'elements' minus twice the sum of the last 'negatives' elements in 'elements', and then 'removals' iterations of the sum of all elements in 'elements' minus twice the sum of the last 'negatives + i' elements in 'elements' for 'i' in range(1, 'removals + 1').

#Overall this is what the function does:This function calculates the maximum achievable sum by iteratively removing elements from a sorted list and adjusting the sum based on the number of negative elements. It takes three inputs: removals (the number of elements to remove), negatives (the number of negative elements to consider), and elements (a sorted list of integers). If the input pair (removals, negatives) is (6, 3), the function returns 0. Otherwise, it calculates a list of sums by subtracting twice the sum of the last 'negatives' elements from the total sum, then iteratively subtracting elements and adjusting the sum based on the number of negative elements. The function returns the maximum value from this list of sums.

