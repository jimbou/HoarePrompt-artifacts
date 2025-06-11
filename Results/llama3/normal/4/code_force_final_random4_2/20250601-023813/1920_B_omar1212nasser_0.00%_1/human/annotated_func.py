#State of the program right berfore the function call: k and x are non-negative integers such that 0 <= k <= n and 0 <= x <= n, and a is a list of integers of length n.
    t = int(input())
    for i in range(t):
        n, k, x = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        a.sort()
        
        product = func_2(k, x, a)
        
        print(product)
        
    #State: n, k, and x are non-negative integers, a is a sorted list of integers of length n, product is the result of func_2(k, x, a), i is t-1, t is at least t, and stdin contains no input, and the product which is the result of func_2(k, x, a) is being printed

#Overall this is what the function does:This function reads input from the user, sorts a list of integers, and then calls another function (func_2) to calculate a product based on the sorted list and other input parameters. The result of the product is then printed to the console. The function iterates this process for a number of test cases specified by the user.

#State of the program right berfore the function call: removals and negatives are non-negative integers, elements is a list of integers sorted in ascending order.
    if (removals == 6 and negatives == 3) :
        return 0
        #The program returns 0
    #State: removals and negatives are non-negative integers, elements is a list of integers sorted in ascending order. The pair (removals, negatives) is not equal to (6, 3).
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
        
    #State: removals is at least 1, i is removals, negatives is a non-negative integer, elements is a list of integers sorted in ascending order, pos is a list containing removals + 1 elements where the first element is the difference between the sum of all elements in 'elements' and twice the sum of the last 'negatives' elements in 'elements', and the rest of the elements are s decreased by the smallest element in elements and then decreased by twice the difference between the (negatives + i)th element from the end and the ith element from the end in elements, s is decreased by the sum of the last removals elements in elements, and n is either increased by the sum of the differences between the (negatives + i)th element from the end and the ith element from the end in elements if negatives + i is not greater than the length of elements, or 0 if negatives + i is out of range.
    return max(pos)
    #The program returns the maximum value from the list 'pos', which contains 'removals + 1' elements. The first element in 'pos' is the difference between the sum of all elements in 'elements' and twice the sum of the last 'negatives' elements in 'elements'. The rest of the elements in 'pos' are calculated by decreasing 's' by the smallest element in 'elements' and then decreasing it by twice the difference between the (negatives + i)th element from the end and the ith element from the end in 'elements', where 's' is also decreased by the sum of the last 'removals' elements in 'elements'. Additionally, 'n' is either increased by the sum of the differences between the (negatives + i)th element from the end and the ith element from the end in 'elements' if 'negatives + i' is not greater than the length of 'elements', or 0 if 'negatives + i' is out of range.

#Overall this is what the function does:This function calculates the maximum possible value that can be obtained by removing a certain number of elements from a sorted list and adjusting the sum of the remaining elements based on the number of negative elements. It takes three parameters: removals, negatives, and elements. If removals is 6 and negatives is 3, it returns 0. Otherwise, it calculates a list of values by subtracting twice the sum of the last negatives elements from the sum of all elements, and then iteratively subtracting the smallest element and twice the difference between the (negatives + i)th element from the end and the ith element from the end. The function returns the maximum value from this list.

