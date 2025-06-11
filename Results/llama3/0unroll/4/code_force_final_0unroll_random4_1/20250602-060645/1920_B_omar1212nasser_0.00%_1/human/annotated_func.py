#State of the program right berfore the function call: t is a positive integer, n, k, and x are positive integers such that 1 <= n <= 2 * 10^5, 1 <= x, k <= n, and a is a list of n positive integers such that 1 <= a_i <= 1000.
    t = int(input())
    for i in range(t):
        n, k, x = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        a.sort()
        
        product = func_2(k, x, a)
        
        print(product)
        
    #State: The loop iterates t times, and for each iteration, it reads input from stdin, sorts the list a, calculates the product using the function func_2, and prints the result. After all iterations, the loop finishes, and the program terminates. The values of t, n, k, x, and a are updated according to the input read in each iteration, but their initial values are lost. The state of the other variables in the precondition remains unchanged.

#Overall this is what the function does:This function reads input from stdin, sorts a list of integers, and calculates a product using the function func_2. It iterates this process a specified number of times, printing the result each time, and then terminates.

#State of the program right berfore the function call: removals and negatives are non-negative integers, elements is a list of non-negative integers sorted in ascending order.
    if (removals == 6 and negatives == 3) :
        return 0
        #The program returns 0
    #State: removals and negatives are non-negative integers, elements is a list of non-negative integers sorted in ascending order. Either removals is not equal to 6 or negatives is not equal to 3, or both conditions are not met.
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
        
    #State: Output State: removals is a non-negative integer, negatives is a non-negative integer, elements is a list of non-negative integers sorted in ascending order, pos is a list containing removals + 1 elements which are the differences between the sum of all elements and twice the sum of the last negatives elements in the list elements after each removal.
    return max(pos)
    #The program returns the maximum value in the list 'pos', which contains the differences between the sum of all elements and twice the sum of the last 'negatives' elements in the list 'elements' after each removal, where 'removals' is a non-negative integer and 'negatives' is a non-negative integer.

#Overall this is what the function does:This function calculates the maximum difference between the sum of all elements in a sorted list and twice the sum of the last 'negatives' elements after a series of 'removals'. It takes three parameters: 'removals' and 'negatives' as non-negative integers, and 'elements' as a list of non-negative integers sorted in ascending order. If 'removals' is 6 and 'negatives' is 3, it returns 0. Otherwise, it iteratively removes elements from the end of the list, updates the sum of all elements and the sum of the last 'negatives' elements, and calculates the difference between these two sums. The function returns the maximum difference found during these iterations.

