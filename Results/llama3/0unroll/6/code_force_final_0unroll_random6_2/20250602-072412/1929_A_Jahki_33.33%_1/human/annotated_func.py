#State of the program right berfore the function call: a is a list of integers, num2 is an integer representing the length of the list a, 2 <= num2 <= 100, and all elements in a are integers between 1 and 10^9.
    order = 0
    for i in range(1, num2):
        if a[i - 1] >= a[i]:
            order += 1
        
    #State: Output State: `a` is a list of integers, `num2` is an integer representing the length of the list `a`, `2 <= num2 <= 100`, all elements in `a` are integers between 1 and 10^9, and `order` is the number of pairs of adjacent elements in `a` where the first element is greater than or equal to the second element.
    if (order == 0) :
        return True
        #The program returns a boolean value True.
    else :
        return False
        #The program returns False

#Overall this is what the function does:This function determines whether a given list of integers is sorted in non-decreasing order. It takes a list of integers and its length as input, and returns a boolean value indicating whether the list is sorted (True) or not (False). The function does not modify the input list.

