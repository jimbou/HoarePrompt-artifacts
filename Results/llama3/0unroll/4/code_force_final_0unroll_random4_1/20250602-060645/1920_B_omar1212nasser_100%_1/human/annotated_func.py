#State of the program right berfore the function call: t is a positive integer, n, k, and x are positive integers, and a is a list of n positive integers.
    t = int(input())
    for i in range(t):
        n, k, x = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        a.sort()
        
        product = func_2(k, x, a)
        
        print(product)
        
    #State: Output State: t executions of the loop have finished, n, k, and x have been updated with the last input values, a is sorted in ascending order based on the last input values, and the product of the last k elements of a and x has been printed t times.

#Overall this is what the function does:This function reads input from the user, sorts a list of integers in ascending order, and calculates the product of the last k elements of the sorted list and an integer x. It repeats this process t times, printing the product after each iteration. The function does not modify the input values n, k, or x, but updates the list a with the last input values.

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
        
    #State: Output State: removals is a non-negative integer, negatives is a non-negative integer, elements is a list of integers sorted in ascending order, pos is a list containing removals + 1 elements where each element is the sum of all elements in elements minus twice the sum of the last negatives elements in elements, s is the sum of all elements in elements minus the sum of the last removals elements in elements, s2 is the sum of the last negatives elements in elements minus the sum of the last removals elements in elements plus the sum of the last removals - negatives elements in elements.
    return max(pos)
    #The program returns the maximum value from the list 'pos', where each element in 'pos' is the sum of all elements in the sorted list 'elements' minus twice the sum of the last 'negatives' elements in 'elements'.

#Overall this is what the function does:Functionality: This function calculates the maximum value that can be obtained by subtracting twice the sum of the last 'negatives' elements from the sum of all elements in a sorted list 'elements', considering different removals of elements from the end of the list. It takes three parameters: 'removals' (the number of elements to remove), 'negatives' (the number of elements to consider for the subtraction), and 'elements' (the sorted list of integers). The function returns the maximum value obtained after considering all possible removals.

