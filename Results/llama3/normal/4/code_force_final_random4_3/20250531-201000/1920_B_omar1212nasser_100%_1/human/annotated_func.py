#State of the program right berfore the function call: k and x are non-negative integers such that 1 <= k <= n and 1 <= x <= n, n is a positive integer, and a is a list of n positive integers.
    t = int(input())
    for i in range(t):
        n, k, x = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        a.sort()
        
        product = func_2(k, x, a)
        
        print(product)
        
    #State: n is a positive integer equal to the first input, k is a non-negative integer such that 1 <= k <= n, x is a non-negative integer such that 1 <= x <= n, a is a sorted list of n positive integers, t is greater than or equal to 0, i is t-1, product is the result of func_2(k, x, a), and the product which is the result of func_2(k, x, a) is being printed.

#Overall this is what the function does:This function takes no parameters and returns no value. It reads a series of inputs from the user, including a number of test cases, and for each test case, it reads the size of a list of integers, a value k, and a value x. It then reads a list of integers, sorts the list, and calls another function (func_2) with k, x, and the sorted list as arguments. The result of this function call is printed to the console. The function repeats this process for the specified number of test cases.

#State of the program right berfore the function call: removals and negatives are non-negative integers, elements is a list of non-negative integers sorted in ascending order.
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
        
    #State: removals is 0, negatives is a non-negative integer, elements is a list of non-negative integers sorted in ascending order, pos is a list containing removals + 1 elements which are the sum of all elements in elements minus twice the sum of the last negatives elements in elements, s is the sum of all elements in elements minus the last removals elements, s2 is the sum of the last negatives elements in elements.
    return max(pos)
    #The program returns the maximum value from the list 'pos', which contains elements that are the sum of all elements in the list 'elements' minus twice the sum of the last 'negatives' elements in 'elements'. The list 'pos' has 'removals + 1' elements.

#Overall this is what the function does:Calculates the maximum value that can be obtained by removing a specified number of elements from a sorted list and subtracting twice the sum of the last 'negatives' elements, considering all possible removals from 0 to the specified number.

