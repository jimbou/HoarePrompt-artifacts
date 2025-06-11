#State of the program right berfore the function call: k and x are non-negative integers such that 0 <= k <= n and 0 <= x <= n, a is a list of n non-negative integers, n is a positive integer.
    t = int(input())
    for i in range(t):
        n, k, x = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        a.sort()
        
        product = func_2(k, x, a)
        
        print(product)
        
    #State: n is an integer, k is an integer, x is an integer, a is a sorted list of n non-negative integers, t is a non-negative integer, i is t-1, product is the result of func_2(k, x, a), and the product which is the result of func_2(k, x, a) is being printed

#Overall this is what the function does:The function takes a list of integers, a non-negative integer k, and a non-negative integer x as input, sorts the list in ascending order, and then calls another function func_2 with k, x, and the sorted list as arguments. The result of func_2 is stored in the variable product and then printed. The function iterates this process for a number of test cases specified by the user.

#State of the program right berfore the function call: removals and negatives are non-negative integers, elements is a list of non-negative integers sorted in ascending order.
    if (removals == 6 and negatives == 3) :
        return 0
        #The program returns the integer 0
    #State: removals and negatives are non-negative integers, elements is a list of non-negative integers sorted in ascending order. The pair (removals, negatives) is not equal to (6, 3).
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
        
    #State: removals is 0, negatives is a non-negative integer, elements is a list of non-negative integers sorted in ascending order, the pair (removals, negatives) is not equal to (6, 3), pos is a list containing removals + 1 elements where the first element is the sum of all elements minus twice the sum of the last negatives elements in the list elements, and the rest of the elements are s - 2 * n, s is decreased by the sum of the last removals elements in the list elements, and n is either increased by the sum of elements[-(negatives + i)] - elements[-i] for i in range(1, removals + 1) or assigned the value 0 if an IndexError occurs.
    return max(pos)
    #The program returns the maximum value in the list 'pos', where 'pos' contains 'removals + 1' elements, the first element is the sum of all elements minus twice the sum of the last 'negatives' elements in the list 'elements', and the rest of the elements are calculated based on the values of 's' and 'n', which are updated based on the values in the list 'elements' and the values of 'removals' and 'negatives'.

#Overall this is what the function does:This function calculates and returns the maximum possible sum of a list of non-negative integers after a series of removals and negations. It takes three parameters: a list of non-negative integers sorted in ascending order, and two non-negative integers representing the number of removals and negations to be performed. The function returns the maximum sum after the removals and negations, or 0 if the removals and negations are 6 and 3, respectively.

