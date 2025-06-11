#State of the program right berfore the function call: k and x are non-negative integers such that 1 <= k <= n and 1 <= x <= n, and a is a list of n non-negative integers.
    t = int(input())
    for i in range(t):
        n, k, x = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        a.sort()
        
        product = func_2(k, x, a)
        
        print(product)
        
    #State: n is an integer greater than 0, k is an integer such that 1 <= k <= n, x is an integer such that 1 <= x <= n, a is a sorted list of n non-negative integers, t is greater than or equal to 0, i is t-1, product is the result of func_2(k, x, a), and the product which is the result of func_2(k, x, a) is being printed.

#Overall this is what the function does:This function takes no parameters and returns no value. It reads a number of test cases, then for each test case, it reads the number of elements, a target value, and a list of non-negative integers. It sorts the list and calls another function (func_2) with the target value, the sorted list, and the number of elements as arguments. The result of func_2 is then printed. The function does not modify the input values.

#State of the program right berfore the function call: removals and negatives are non-negative integers, elements is a list of integers sorted in ascending order.
    pos = []
    s = sum(elements)
    pos.append(s - 2 * sum(elements[-negatives:]))
    s2 = sum(elements[-negatives:])
    for i in range(1, removals + 1):
        s -= elements[-i]
        
        s2 -= elements[-i]
        
        if negatives + i <= len(elements):
            s2 += elements[-(negatives + i)]
        
        pos.append(s - 2 * s2)
        
    #State: removals is 0, negatives is a non-negative integer, elements is a list of integers sorted in ascending order, pos is a list containing removals + 1 elements where the first element is the sum of all elements in elements minus twice the sum of the last negatives elements in elements, and the rest of the elements are the sum of all elements in elements minus the last i elements minus twice the sum of the last negatives elements in elements minus the last i elements plus the element at index -(negatives + i) in elements if negatives + i is less than or equal to the length of elements, otherwise the rest of the elements are the sum of all elements in elements minus the last i elements minus twice the sum of the last negatives elements in elements minus the last i elements, s is the sum of all elements in elements minus the last removals elements, s2 is the sum of the last negatives elements in elements minus the last removals elements plus the sum of elements at indices -(negatives + i) in elements if negatives + i is less than or equal to the length of elements for i in range(1, removals + 1), otherwise s2 is the sum of the last negatives elements in elements minus the last removals elements, and i is removals.
    return max(pos)
    #The program returns the maximum value from the list 'pos', which contains elements calculated based on the list 'elements', the number of removals, and the number of negatives. The maximum value is the largest sum of all elements in 'elements' minus the last 'i' elements minus twice the sum of the last 'negatives' elements in 'elements' minus the last 'i' elements, plus the element at index -(negatives + i) in 'elements' if negatives + i is less than or equal to the length of 'elements', otherwise the maximum value is the largest sum of all elements in 'elements' minus the last 'i' elements minus twice the sum of the last 'negatives' elements in 'elements' minus the last 'i' elements.

#Overall this is what the function does:Calculates the maximum sum of elements in a sorted list, considering removals and negatives. The function takes a sorted list of integers, a non-negative integer for removals, and a non-negative integer for negatives. It returns the maximum value from a list of sums, where each sum is calculated by subtracting the last 'i' elements and twice the sum of the last 'negatives' elements, and adding the element at index -(negatives + i) if within bounds. The function effectively determines the largest possible sum after removing elements and accounting for negative values.

