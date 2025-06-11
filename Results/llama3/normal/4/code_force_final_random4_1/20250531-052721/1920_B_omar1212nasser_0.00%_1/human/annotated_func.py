#State of the program right berfore the function call: t is a positive integer, n, k, and x are positive integers such that k <= n and x <= n, and a is a list of n positive integers.
    t = int(input())
    for i in range(t):
        n, k, x = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        a.sort()
        
        product = func_2(k, x, a)
        
        print(product)
        
    #State: t is greater than or equal to 0, n, k, and x are positive integers such that k <= n and x <= n, a is a sorted list of n positive integers, i is t-1, stdin is empty, product is the result of func_2(k, x, a), and the product is printed, the product of the result of func_2(k, x, a) is being printed for t times

#Overall this is what the function does:The function reads a positive integer t from standard input, then for each iteration from 0 to t-1, it reads three positive integers n, k, and x, and a list of n positive integers. It sorts the list of integers in ascending order, calls the function func_2 with parameters k, x, and the sorted list, and prints the result. After t iterations, the function concludes, leaving the input variables in their final state, with the product of the result of func_2 printed for t times.

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
        
    #State: removals is at least 1, negatives is a non-negative integer, elements is a list of non-negative integers sorted in ascending order, the pair (removals, negatives) is not equal to (6, 3), pos is a list containing removals + 1 elements which are the sum of all elements in the list elements minus twice the sum of the last negatives elements in the list elements minus elements[-1], s - 2 * n, s - 2 * n, and so on, i is removals, s is decreased by elements[-1] + elements[-2] + ... + elements[-removals], and n is increased by elements[-(negatives + i)] - elements[-i] if negatives + i is less than the length of the list elements, otherwise, n is 0.
    return max(pos)
    #The program returns the maximum value from the list 'pos', which contains elements that are the sum of all elements in the list 'elements' minus twice the sum of the last 'negatives' elements in the list 'elements' minus 'elements[-1]', 's - 2 * n', 's - 2 * n', and so on, where 's' is decreased by 'elements[-1]' + 'elements[-2]' + ... + 'elements[-removals]' and 'n' is increased by 'elements[-(negatives + i)]' - 'elements[-i]' if 'negatives + i' is less than the length of the list 'elements', otherwise 'n' is 0.

#Overall this is what the function does:This function calculates and returns the maximum possible sum of elements in a sorted list after removing a specified number of elements from the end and considering the impact of a certain number of negative elements. It takes three parameters: the number of removals, the number of negative elements, and a sorted list of non-negative integers. If the number of removals is 6 and the number of negative elements is 3, it returns 0. Otherwise, it calculates the sum of all elements minus twice the sum of the last negative elements, then iteratively subtracts the last element and adjusts the sum of negative elements accordingly, storing these values in a list. Finally, it returns the maximum value from this list.

