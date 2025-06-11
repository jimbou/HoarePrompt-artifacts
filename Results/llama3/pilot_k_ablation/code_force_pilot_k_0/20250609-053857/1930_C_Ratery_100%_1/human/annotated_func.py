#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer (n) and then a list of n integers. n is a positive integer and does not exceed 3 * 10^5. The sum of n over all test cases does not exceed 3 * 10^5.
    n = int(input())
    arr = list(map(sum, enumerate(map(int, input().split()), start=1)))
    arr.sort(reverse=True)
    ans = [arr[0]]
    for x in arr[1:]:
        if x >= ans[-1]:
            ans.append(ans[-1] - 1)
        else:
            ans.append(x)
        
    #State: Output State: The output state is a list of integers, where each integer is either the largest integer in the input list or one less than the previous integer in the output list, whichever is smaller. The list is in ascending order. The number of elements in the output list is one more than the number of elements in the input list.
    print(*ans)
    #This is printed: A list of integers in ascending order, where each integer is either the largest integer in the input list or one less than the previous integer in the output list, whichever is smaller. The list has one more element than the input list.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of a positive integer n and a list of n integers. It processes each test case by sorting the list in descending order, then generates a new list where each element is either the largest integer in the input list or one less than the previous element in the output list, whichever is smaller. The function prints the resulting list in ascending order, which has one more element than the input list.

