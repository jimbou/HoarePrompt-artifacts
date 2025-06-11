#State of the program right berfore the function call: stdin contains one input: a non-negative integer.
    return int(input())
    #The program returns a non-negative integer that was provided as input.

#Overall this is what the function does:Reads a non-negative integer from standard input and returns it as an integer value.

#State of the program right berfore the function call: stdin contains a space-separated list of integers.
    return map(int, input().split())
    #The program returns a map object that contains a list of integers that were inputted from stdin, each integer was separated by a space.

#Overall this is what the function does:Reads a space-separated list of integers from standard input and returns a map object containing the input integers.

#State of the program right berfore the function call: stdin contains a space-separated list of integers.
    return list(map(int, input().split()))
    #The program returns a list of integers that were provided as a space-separated list in the standard input.

#Overall this is what the function does:Reads a space-separated list of integers from standard input and returns the list of integers.

#State of the program right berfore the function call: stdin contains a space-separated list of integers.
    return sorted(list(map(int, input().split())))
    #The program returns a sorted list of integers that were in the space-separated list of integers in stdin.

#Overall this is what the function does:Reads a space-separated list of integers from standard input, sorts them in ascending order, and returns the sorted list.

#State of the program right berfore the function call: stdin contains a space-separated list of strings
    return map(str, input().split())
    #The program returns a map object containing a list of strings, where each string is a word from the space-separated list of strings in stdin.

#Overall this is what the function does:The function reads a space-separated list of strings from standard input, splits it into individual words, and returns a map object containing these words as strings.

#State of the program right berfore the function call: stdin contains a string
    return list(input())
    #The program returns a list of characters in the string from stdin.

#Overall this is what the function does:The function reads a string from standard input and returns it as a list of characters.

#State of the program right berfore the function call: stdin contains a space-separated list of strings.
    return sorted(list(map(str, input().split())))
    #The program returns a list of strings from stdin, sorted in ascending order, where each string is separated by a space.

#Overall this is what the function does:The function reads a space-separated list of strings from standard input, sorts them in ascending order, and returns the sorted list.

#State of the program right berfore the function call: arr is a list of non-negative integers.
    ans = []
    tem = 1
    for i in range(len(arr)):
        tem *= arr[i]
        
        ans.append(tem)
        
    #State: arr is a list of non-negative integers, ans is a list containing the product of the first element of arr and 1, the product of the first two elements of arr and 1, the product of the first three elements of arr and 1, ..., the product of all elements of arr and 1, tem is the product of all elements of arr and 1, i is the last index of arr.
    return ans
    #The program returns a list 'ans' containing the cumulative product of all elements in list 'arr' and 1, where 'arr' is a list of non-negative integers.

#Overall this is what the function does:This function calculates the cumulative product of a list of non-negative integers and returns the result as a new list. The function takes a list of non-negative integers as input, multiplies each element by the cumulative product of all previous elements, and returns a new list containing these cumulative products. The input list remains unchanged. The function returns a list of the same length as the input list, where each element is the product of all elements up to that point in the input list.

#State of the program right berfore the function call: arr is a list of non-negative integers.
    ans = []
    tem = 1
    for i in range(len(arr) - 1, -1, -1):
        tem *= arr[i]
        
        ans.append(tem)
        
    #State: arr is a list of non-negative integers, ans is a list containing the product of all elements of arr, tem is the product of all elements of arr, i is -1
    return ans
    #The program returns a list containing the product of all non-negative integers in the list 'arr'.

#Overall this is what the function does:This function takes a list of non-negative integers as input and returns a new list containing the product of all elements in the input list. The input list remains unchanged. The returned list contains the cumulative product of the input list elements in reverse order.

