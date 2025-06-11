#State of the program right berfore the function call: k and x are non-negative integers such that 1 <= k <= n and 1 <= x <= n, and a is a list of n non-negative integers.
    t = int(input())
    for i in range(t):
        n, k, x = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        a.sort()
        
        product = func_2(k, x, a)
        
        print(product)
        
    #State: n is an integer greater than 0, k is a non-negative integer such that 1 <= k <= n, x is a non-negative integer such that 1 <= x <= n, a is a sorted list of n non-negative integers, t is an integer greater than or equal to 0, i is t-1, product is the result of func_2(k, x, a), and the product which is the result of func_2(k, x, a) is being printed.

#Overall this is what the function does:The function accepts a list of non-negative integers and two non-negative integers k and x, such that 1 <= k <= n and 1 <= x <= n, where n is the length of the list. It sorts the list in ascending order and then calls another function, func_2, with k, x, and the sorted list as arguments. The result of func_2 is then printed. The function iterates this process for a specified number of test cases, t.

#State of the program right berfore the function call: removals and negatives are non-negative integers, and elements is a list of non-negative integers sorted in ascending order.
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
        
    #State: removals is a non-negative integer that must be at least removals, negatives is a non-negative integer, elements is a list of non-negative integers sorted in ascending order, pos is a list containing removals + 1 elements: the sum of all elements minus twice the sum of the last 'negatives' elements in the list 'elements', and removals sums of all elements minus twice the sum of the last 'negatives' elements in the list 'elements' minus twice the sum of the last 'negatives' elements in the list 'elements' minus the last element plus the element at index -(negatives + i), s is the sum of all elements in the list 'elements' minus the sum of the last 'removals' elements, s2 is the sum of the last 'negatives' elements in the list 'elements' minus the sum of the last 'removals' elements plus the sum of elements at index -(negatives + i) for i from 1 to removals.
    return max(pos)
    #The program returns the maximum value from the list 'pos', which contains elements that are calculated based on the sum of all elements in the list 'elements', the sum of the last 'negatives' elements, the sum of the last 'removals' elements, and the elements at specific indices in the list 'elements'.

#Overall this is what the function does:This function calculates and returns the maximum value from a list of sums, where each sum is calculated by subtracting twice the sum of the last 'negatives' elements in the list 'elements' from the sum of all elements in the list 'elements', and then iteratively subtracting the last 'removals' elements and adding the element at index -(negatives + i) for i from 1 to removals. The function takes three parameters: 'removals' and 'negatives' as non-negative integers, and 'elements' as a list of non-negative integers sorted in ascending order. The function returns the maximum value from the calculated list of sums.

