#State of the program right berfore the function call: k and x are non-negative integers such that 1 <= k <= n and 1 <= x <= n, and a is a list of n non-negative integers.
    t = int(input())
    for i in range(t):
        n, k, x = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        a.sort()
        
        product = func_2(k, x, a)
        
        print(product)
        
    #State: Output State: The values of n, k, and x have been updated t times with new input values, and the list a has been updated t times with new sorted lists of non-negative integers. The variable product has been printed t times, each time with the result of the function func_2 applied to the current values of k, x, and a.

#Overall this is what the function does:This function reads input from the user, sorts a list of non-negative integers, and applies another function (func_2) to the sorted list and two input integers (k and x), printing the result. It repeats this process a specified number of times (t), updating the input values and list each time.

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
        
    #State: Output State: removals is a non-negative integer, negatives is a non-negative integer, elements is a list of integers sorted in ascending order, pos is a list containing 'removals + 1' elements which are the sum of all elements in the list minus twice the sum of the last 'negatives' elements in the list, s is the sum of all elements in the list minus the sum of the last 'removals' elements in the list, s2 is the sum of the last 'negatives' elements in the list minus the sum of the last 'removals' elements in the list plus the sum of the last 'removals' elements in the list if 'negatives' plus 'removals' is less than or equal to the length of the list.
    return max(pos)
    #The program returns the maximum value from the list 'pos', which contains 'removals + 1' elements that are the sum of all elements in the list minus twice the sum of the last 'negatives' elements in the list.

#Overall this is what the function does:Calculates the maximum sum of all elements in a sorted list minus twice the sum of the last 'negatives' elements, considering 'removals' number of elements removed from the end of the list.

