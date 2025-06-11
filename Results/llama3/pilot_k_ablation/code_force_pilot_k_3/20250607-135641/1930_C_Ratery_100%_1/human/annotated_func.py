#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer (the length of array a) and then a list of integers (the elements of array a). The length of array a is a non-negative integer and the elements of array a are non-negative integers.
    n = int(input())
    arr = list(map(sum, enumerate(map(int, input().split()), start=1)))
    arr.sort(reverse=True)
    ans = [arr[0]]
    for x in arr[1:]:
        if x >= ans[-1]:
            ans.append(ans[-1] - 1)
        else:
            ans.append(x)
        
    #State: stdin contains multiple test cases minus one, n is a non-negative integer, arr is an empty list, ans is a list containing the largest element of the original arr, either the second largest element of the original arr or ans[-2] - 1, either the third largest element of the original arr or ans[-1] - 1, and so on, until the last element of the original arr or ans[-1] - 1, depending on whether each element of the original arr is less than or greater than or equal to ans[-1].
    print(*ans)
    #This is printed: The elements of the ans list which contains the largest element of the original arr, either the second largest element of the original arr or ans[-2] - 1, either the third largest element of the original arr or ans[-1] - 1, and so on, until the last element of the original arr or ans[-1] - 1, depending on whether each element of the original arr is less than or greater than or equal to ans[-1]

#Overall this is what the function does:The function reads a sequence of test cases from standard input, where each test case consists of an integer (n) followed by a list of integers (a). It then processes each test case by sorting the list in descending order and creating a new list (ans) where each element is either the corresponding element from the original list or one less than the previous element in ans, whichever is smaller. The function prints the elements of ans for each test case.

