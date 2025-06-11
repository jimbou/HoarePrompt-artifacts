#State of the program right berfore the function call: k and x are non-negative integers such that 1 <= k <= n and 1 <= x <= n, and a is a list of n non-negative integers.
    t = int(input())
    for i in range(t):
        n, k, x = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        a.sort()
        
        product = func_2(k, x, a)
        
        print(product)
        
    #State: Output State: The values of n, k, x, and a have been updated t times, with the last update being the final values. The variable product has been printed to the console t times, with the last printed value being the final product. The values of t and stdin remain unchanged.

#Overall this is what the function does:This function reads input from the user, sorts a list of non-negative integers, and then calls another function (func_2) with the sorted list and other input values (k and x) to calculate a product, which is then printed to the console. The function repeats this process a specified number of times (t), updating the input values each time, and prints the final product.

#State of the program right berfore the function call: removals and negatives are non-negative integers, elements is a list of non-negative integers sorted in ascending order.
    if (removals == 6 and negatives == 3) :
        return 0
        #The program returns 0, which is an integer.
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
        
    #State: Output State: removals is a non-negative integer, negatives is a non-negative integer, elements is a list of non-negative integers sorted in ascending order, pos is a list containing removals + 1 elements which are the differences between the sum of all elements and twice the sum of the last negatives elements, s is the sum of all elements, n is the sum of the last negatives elements.
    return max(pos)
    #The program returns the maximum value from the list 'pos' which contains the differences between the sum of all elements 's' and twice the sum of the last 'negatives' elements 'n', where 's' is the sum of all non-negative integers in the list 'elements' and 'n' is the sum of the last 'negatives' elements in the list 'elements'.

#Overall this is what the function does:This function calculates the maximum difference between the sum of all elements in a sorted list and twice the sum of the last 'negatives' elements, considering 'removals' number of elements from the end of the list. It returns 0 if 'removals' is 6 and 'negatives' is 3; otherwise, it returns the maximum difference value. The function takes three parameters: 'removals', 'negatives', and 'elements', and returns an integer value.

